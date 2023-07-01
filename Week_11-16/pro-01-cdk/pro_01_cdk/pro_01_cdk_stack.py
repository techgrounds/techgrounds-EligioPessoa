# Import necessary libraries and modules

from aws_cdk import NestedStack, Stack, aws_ec2 as ec2, aws_s3 as s3
from constructs import Construct
import pro_01_cdk.config as config
import aws_cdk as cdk

# Define the main AWS Cloud Development Kit (CDK) stack

class Pro01CdkStack(Stack):
    # Constructor method
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Setup the VPCs
        self.setup_vpc()

        # Attach internet gateways to the created VPCs

        self.internet_gateways = self.attach_internet_gateways()

        # Define dictionaries for storing subnet and route table data

        self.subnet_id_to_subnet_map = {}

        # Call methods to create route tables, subnets, their associations, and routes  
          
        self.route_table_id_to_route_table_map = {}
        self.create_route_tables()
        self.create_subnets()
        self.create_subnet_route_table_associations()
        self.create_routes()
        
        self.setup_security_group()
        self.setup_ec2()
        self.setup_peering()
        self.setup_s3_bucket()

        
        # Setting up VPCs, subnets and route tables
    def setup_vpc(self):
        # Create production VPC with a specific IP range
        self.prod_vpc = ec2.Vpc(
            # Assign the VPC parameters such as the CIDR, and DNS support
            self, "ProdVPC", ip_addresses=ec2.IpAddresses.cidr('10.10.10.0/24'),
            subnet_configuration=[],
            enable_dns_support=True,
            enable_dns_hostnames=True,            
        )
        # Create management VPC with a specific IP range
        self.mgmt_vpc = ec2.Vpc(
            # Assign the VPC parameters such as the CIDR, and DNS support
            self, "MgmtVPC", ip_addresses=ec2.IpAddresses.cidr('10.20.20.0/24'),
            nat_gateways=0, subnet_configuration=[],
            enable_dns_support=True,
            enable_dns_hostnames=True,
        )        




    # Method to create route tables using provided configurations

    def create_route_tables(self):
        # (This method creates route tables for the production and management VPCs)
        for route_table_id in config.ROUTE_TABLES_ID_TO_ROUTES_MAP_1:
            self.route_table_id_to_route_table_map[route_table_id] = ec2.CfnRouteTable(
                self, route_table_id, vpc_id=self.prod_vpc.vpc_id,
                tags=[{'key': 'Name', 'value': route_table_id}]
            )
        for route_table_id in config.ROUTE_TABLES_ID_TO_ROUTES_MAP_2:
            self.route_table_id_to_route_table_map[route_table_id] = ec2.CfnRouteTable(
                self, route_table_id, vpc_id=self.mgmt_vpc.vpc_id,
                tags=[{'key': 'Name', 'value': route_table_id}]
            )

    def create_routes(self):
        # (This method creates the routes for the route tables of both VPCs)    
        for route_table_id, routes in config.ROUTE_TABLES_ID_TO_ROUTES_MAP_1.items():
            for i in range(len(routes)):
                route = routes[i]
                kwargs = {
                    **route,
                    'route_table_id': self.route_table_id_to_route_table_map[route_table_id].ref,
                }
                if route['router_type'] == ec2.RouterType.GATEWAY:
                    kwargs['gateway_id'] = self.internet_gateways[config.INTERNET_GATEWAY_1].ref
                if route['router_type'] == ec2.RouterType.NAT_GATEWAY:
                    kwargs['nat_gateway_id'] = self.nat_gateway.ref
                del kwargs['router_type']
                ec2.CfnRoute(self, f'{route_table_id}-route-{i}', **kwargs)
        for route_table_id, routes in config.ROUTE_TABLES_ID_TO_ROUTES_MAP_2.items():
            for i in range(len(routes)):
                route = routes[i]
                kwargs = {
                    **route,
                    'route_table_id': self.route_table_id_to_route_table_map[route_table_id].ref,
                }
                if route['router_type'] == ec2.RouterType.GATEWAY:
                    kwargs['gateway_id'] = self.internet_gateways[config.INTERNET_GATEWAY_2].ref
                if route['router_type'] == ec2.RouterType.NAT_GATEWAY:
                    kwargs['nat_gateway_id'] = self.nat_gateway.ref
                del kwargs['router_type']
                ec2.CfnRoute(self, f'{route_table_id}-route-{i}', **kwargs)
                


     # Method to attach internet gateways to the VPCs

    def attach_internet_gateways(self):
        internet_gateway_1 = ec2.CfnInternetGateway(self, config.INTERNET_GATEWAY_1)
        ec2.CfnVPCGatewayAttachment(self, f'{config.INTERNET_GATEWAY_1}-attachment',
                                    vpc_id=self.prod_vpc.vpc_id,
                                    internet_gateway_id=internet_gateway_1.ref)
        internet_gateway_2 = ec2.CfnInternetGateway(self, config.INTERNET_GATEWAY_2)
        ec2.CfnVPCGatewayAttachment(self, f'{config.INTERNET_GATEWAY_2}-attachment',
                                    vpc_id=self.mgmt_vpc.vpc_id,
                                    internet_gateway_id=internet_gateway_2.ref)    
        return { 
            config.INTERNET_GATEWAY_1: internet_gateway_1,
            config.INTERNET_GATEWAY_2: internet_gateway_2
        }

    # Method to create subnets within the VPCs
    def create_subnets(self):
        # (This method creates subnets in both VPCs based on configuration files)
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION_1.items():
            subnet = ec2.CfnSubnet(
                self, subnet_id, vpc_id=self.prod_vpc.vpc_id,
                cidr_block=subnet_config['cidr_block'],
                availability_zone=subnet_config['availability_zone'],
                tags=[{'key': 'Name', 'value': subnet_id}],
                map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
            )
            self.subnet_id_to_subnet_map[subnet_id] = subnet

        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION_2.items():
            subnet = ec2.CfnSubnet(
                self, subnet_id, vpc_id=self.mgmt_vpc.vpc_id,
                cidr_block=subnet_config['cidr_block'],
                availability_zone=subnet_config['availability_zone'],
                tags=[{'key': 'Name', 'value': subnet_id}],
                map_public_ip_on_launch=subnet_config['map_public_ip_on_launch'],
            )
            self.subnet_id_to_subnet_map[subnet_id] = subnet        

    # Method to create subnet-route table associations

    def create_subnet_route_table_associations(self):
        # (This method associates subnets with route tables in both VPCs)
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION_1.items():
            route_table_id = subnet_config['route_table_id']
            ec2.CfnSubnetRouteTableAssociation(
                self, f'{subnet_id}-{route_table_id}',
                subnet_id=self.subnet_id_to_subnet_map[subnet_id].ref,
                route_table_id=self.route_table_id_to_route_table_map[route_table_id].ref
            )
        for subnet_id, subnet_config in config.SUBNET_CONFIGURATION_2.items():
            route_table_id = subnet_config['route_table_id']
            ec2.CfnSubnetRouteTableAssociation(
                self, f'{subnet_id}-{route_table_id}',
                subnet_id=self.subnet_id_to_subnet_map[subnet_id].ref,
                route_table_id=self.route_table_id_to_route_table_map[route_table_id].ref
            )

        # Fetching references to the subnets where we intend to deploy our servers
        self.subnet_webserver = self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_1].ref
        self.subnet_mgmtserver = self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_3].ref

        amzn_linux_ami = ec2.AmazonLinuxImage(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
        ).get_image(self).image_id

    def setup_security_group(self):
        # Create a security group in the production VPC
        self.security_group_prod = ec2.SecurityGroup(
            self,
            "SecurityGroupProd",
            vpc=self.prod_vpc,
            description="Allow HTTP access from anywhere and all outbound",
            )

        # Open port 80 (HTTP) on the security group for incoming traffic from any IP
        self.security_group_prod.connections.allow_from_any_ipv4(ec2.Port.tcp(80))

        # Create a security group for the management instance in the management VPC
        self.security_group_mgmt = ec2.SecurityGroup(
            self,
            "SecurityGroupMgmt",
            vpc=self.mgmt_vpc,
            description="Allow SSH access from anywhere and all outbound",
        )

        # Open port 22 (SSH) on the security group for incoming traffic from any IP
        self.security_group_mgmt.connections.allow_from_any_ipv4(ec2.Port.tcp(22))

    # Create EC2 instances
    def setup_ec2(self):
        # Define AMI (Amazon Machine Image) for the EC2 instances
        amzn_linux_ami = ec2.AmazonLinuxImage(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
        ).get_image(self).image_id

        # Define a new KeyPair
        key_pair = ec2.CfnKeyPair(self, "MyKeyPair",
            key_name="mykeypair"
        )

        # Create Web server 
        web_server = ec2.CfnInstance(self, "Web_Server",
                        instance_type="t2.micro",
                        image_id=amzn_linux_ami,
                        key_name=key_pair.key_name,
                        subnet_id=self.subnet_webserver,
                        security_group_ids=[self.security_group_prod.security_group_id],
                        user_data=cdk.Fn.base64('''#!/bin/bash
                                    # Install Apache Web Server and PHP
                                    yum install -y httpd mysql php
                                    # Download Lab files
                                    wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
                                    unzip lab-app.zip -d /var/www/html/
                                    # Turn on web server
                                    chkconfig httpd on
                                    service httpd start'''),
                        tags=[{"key": "Name", "value": "Web_Server"}])

        # Allocate an Elastic IP for the Web server
        web_server_eip = ec2.CfnEIP(self, "WebServerEIP", instance_id=web_server.ref)
        
        # Create Management server
        mgmt_server = ec2.CfnInstance(self, "Management_Server",
                        instance_type="t2.micro",
                        image_id=amzn_linux_ami,
                        subnet_id=self.subnet_mgmtserver,
                        security_group_ids=[self.security_group_mgmt.security_group_id],
                        tags=[{"key": "Name", "value": "Management_Server"}])


    
        # Allow SSH and RDP access from the management server to the production server
        self.security_group_prod.connections.allow_from(
            self.security_group_mgmt, 
            ec2.Port.tcp(22), 
            "Allow SSH access from Management Server"
        )

        self.security_group_prod.connections.allow_from(
            self.security_group_mgmt, 
            ec2.Port.tcp(3389), 
            "Allow RDP access from Management Server"
        )

        # Create a network peering stack which creates peering between the production and management VPCs
    def setup_peering(self):
        self.peering_stack = NetworkPeeringStack(
            self,
            "NetworkPeeringStack",
            vpc_one=self.prod_vpc,
            vpc_two=self.mgmt_vpc,
            route_table_id_to_route_table_map=self.route_table_id_to_route_table_map                        
        )

    def setup_s3_bucket(self):
        # Create an S3 bucket for storing post deployment scripts
        bucket = s3.Bucket(self, "PostDeploymentScripts",
        versioned=True,
        removal_policy=cdk.RemovalPolicy.DESTROY,
        auto_delete_objects=True,
        bucket_name="postdeploymentscripts")

        # Get subnet IDs of the management VPC
        subnet_ids_mgmt_vpc = [self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_3].ref,
                            self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_4].ref]

# Define the peering stack which establishes peering between two VPCs

class NetworkPeeringStack(NestedStack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc_one: ec2.Vpc,
        vpc_two: ec2.Vpc,
        route_table_id_to_route_table_map: dict,        
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # set it as an instance variable
        self.route_table_id_to_route_table_map = route_table_id_to_route_table_map

         # Create peering connection between two VPCs
        self.peerconnection = ec2.CfnVPCPeeringConnection(
            self,
            "Peering Connection",
            vpc_id=vpc_one.vpc_id,
            peer_vpc_id=vpc_two.vpc_id,
            
        )
        # Create routes in the peered VPCs for traffic flow
        ec2.CfnRoute(
            self,
            "RouteFromProdtoMgmt",
            destination_cidr_block=vpc_one.vpc_cidr_block,
            route_table_id=self.route_table_id_to_route_table_map[config.PUBLIC_ROUTE_TABLE_2].ref,
            vpc_peering_connection_id=self.peerconnection.ref,
        )

        ec2.CfnRoute(
            self,
            "RouteFromMgmttoProd",
            destination_cidr_block=vpc_two.vpc_cidr_block,
            route_table_id=self.route_table_id_to_route_table_map[config.PUBLIC_ROUTE_TABLE_1].ref,
            vpc_peering_connection_id=self.peerconnection.ref,
        )
        
