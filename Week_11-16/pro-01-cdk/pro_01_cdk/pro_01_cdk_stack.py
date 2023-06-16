from aws_cdk import NestedStack, Stack, aws_ec2 as ec2, aws_rds as rds, aws_s3 as s3
from constructs import Construct
import pro_01_cdk.config as config
import aws_cdk as cdk



class Pro01CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

                
        # Create VPC with 2 public subnets for web server


        # create VPC

        self.prod_vpc = ec2.Vpc(
            self, "ProdVPC", ip_addresses=ec2.IpAddresses.cidr('10.10.10.0/24'),
            subnet_configuration=[],
            enable_dns_support=True,
            enable_dns_hostnames=True,            
        )
       

        self.mgmt_vpc = ec2.Vpc(
            self, "MgmtVPC", ip_addresses=ec2.IpAddresses.cidr('10.20.20.0/24'),
            nat_gateways=0, subnet_configuration=[],
            enable_dns_support=True,
            enable_dns_hostnames=True,
        )        

        self.internet_gateways = self.attach_internet_gateways()

        self.subnet_id_to_subnet_map = {}    
        self.route_table_id_to_route_table_map = {}
        self.create_route_tables()

        self.create_subnets()
        self.create_subnet_route_table_associations()

        self.create_routes()

    def create_route_tables(self):
        """ Create Route Tables """
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
        """ Create routes of the Route Tables """
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


    def create_subnets(self):
        """ Create subnets of the VPC """
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

    def create_subnet_route_table_associations(self):
        """ Associate subnets with route tables """
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

        # Creation of EC2 instance:
        subnet_webserver = self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_1].ref
        subnet_mgmtserver = self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_3].ref

        amzn_linux_ami = ec2.AmazonLinuxImage(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
        ).get_image(self).image_id

        # Security group
        security_group_prod = ec2.SecurityGroup(
            self,
            "SecurityGroupProd",
            vpc=self.prod_vpc,
            description="Allow HTTP access from anywhere and all outbound",
            )



        web_server = ec2.CfnInstance(self, "Web_Server",
                        instance_type="t2.micro",
                        image_id=amzn_linux_ami,
                        subnet_id=subnet_webserver,
                        security_group_ids=[security_group_prod.security_group_id],
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

        mgmt_server = ec2.CfnInstance(self, "Management_Server",
                        instance_type="t2.micro",
                        image_id=amzn_linux_ami,
                        subnet_id=subnet_mgmtserver,
                        tags=[{"key": "Name", "value": "Management_Server"}])         

        # Allow inbound HTTP access from anywhere
        
        security_group_prod.connections.allow_from_any_ipv4(ec2.Port.tcp(80))


        # Peering Stack
        self.peering_stack = NetworkPeeringStack(
            self,
            "NetworkPeeringStack",
            vpc_one=self.prod_vpc,
            vpc_two=self.mgmt_vpc,
            route_table_id_to_route_table_map=self.route_table_id_to_route_table_map
            
            
        )

        bucket = s3.Bucket(self, "PostDeploymentScripts",
        versioned=True,
        removal_policy=cdk.RemovalPolicy.DESTROY,
        auto_delete_objects=True,
        bucket_name="postdeploymentscripts")

        subnet_ids_mgmt_vpc = [self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_3].ref,
            self.subnet_id_to_subnet_map[config.PUBLIC_SUBNET_4].ref]


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

        # Peering connection
        self.peerconnection = ec2.CfnVPCPeeringConnection(
            self,
            "Peering Connection",
            vpc_id=vpc_one.vpc_id,
            peer_vpc_id=vpc_two.vpc_id,
            
        )

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
        