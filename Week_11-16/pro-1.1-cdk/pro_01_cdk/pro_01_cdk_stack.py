from aws_cdk import NestedStack, Stack, aws_ec2 as ec2, aws_rds as rds, aws_s3 as s3
from constructs import Construct
import aws_cdk as cdk
from aws_cdk import aws_elasticloadbalancingv2 as elbv2, aws_autoscaling as autoscaling
from aws_cdk import aws_events as events, aws_events_targets as targets
from aws_cdk import aws_backup as backup
from aws_cdk import aws_iam as iam
from aws_cdk import aws_kms as kms
from aws_cdk import aws_autoscaling_common as common
from aws_cdk import aws_cloudwatch as cloudwatch
from aws_cdk import aws_certificatemanager as acm



class Pro01CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.setup_vpc()
        self.setup_peering()
        self.setup_kms()
        #self.setup_iam()
        self.setup_security_group()
        self.setup_ec2()
        self.setup_s3_bucket()
        self.setup_load_balancer()
        self.setup_db()
        self.setup_backup()

    def setup_vpc(self):    
        # Public - NAT
        self.prod_vpc = ec2.Vpc(
            self,
            "Network1",
            ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public Subnet",
                ),
                
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    name="Private Subnet",
                ),               
            ],            
            availability_zones=["eu-central-1a", "eu-central-1b" , "eu-central-1c"],
            nat_gateways=0,
        )

        
        self.mgmt_vpc = ec2.Vpc(
            self,
            "Network2",
            ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public Subnet"                    
                ),                
            ],
            availability_zones=["eu-central-1a", "eu-central-1b"],            
        )
        '''
        # Create NACL for prod_vpc
        prod_vpc_nacl = ec2.NetworkAcl(self, "ProdVpcNACL", vpc=self.prod_vpc)

        prod_vpc_nacl.add_entry("ProdVpcInboundRule1", cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block), rule_number=120, traffic=ec2.AclTraffic.tcp_port_range(80, 80), direction=ec2.TrafficDirection.INGRESS)
        prod_vpc_nacl.add_entry("ProdVpcInboundRule2", cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block), rule_number=110, traffic=ec2.AclTraffic.tcp_port_range(1024, 65535), direction=ec2.TrafficDirection.INGRESS)
        prod_vpc_nacl.add_entry("ProdVpcOutboundRule1", cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block), rule_number=120, traffic=ec2.AclTraffic.tcp_port_range(80, 80), direction=ec2.TrafficDirection.EGRESS)
        prod_vpc_nacl.add_entry("ProdVpcOutboundRule2", cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block), rule_number=110, traffic=ec2.AclTraffic.tcp_port_range(1024, 65535), direction=ec2.TrafficDirection.EGRESS)


        # Add rules to allow inbound and outbound traffic from select IP addresses
        prod_vpc_nacl.add_entry("ProdVpcInboundRule3", cidr=ec2.AclCidr.ipv4("82.75.30.6/32"), rule_number=200, traffic=ec2.AclTraffic.all_traffic(), direction=ec2.TrafficDirection.INGRESS)
        prod_vpc_nacl.add_entry("ProdVpcOutboundRule3", cidr=ec2.AclCidr.ipv4("82.75.30.6/32"), rule_number=200, traffic=ec2.AclTraffic.all_traffic(), direction=ec2.TrafficDirection.EGRESS)

        # Add rules to allow inbound and outbound traffic between prod_vpc and mgmt_vpc
        prod_vpc_nacl.add_entry("ProdVpcInboundRule4", cidr=ec2.AclCidr.ipv4(self.mgmt_vpc.vpc_cidr_block), rule_number=199, traffic=ec2.AclTraffic.all_traffic(), direction=ec2.TrafficDirection.INGRESS)
        prod_vpc_nacl.add_entry("ProdVpcOutboundRule4", cidr=ec2.AclCidr.ipv4(self.mgmt_vpc.vpc_cidr_block), rule_number=199, traffic=ec2.AclTraffic.all_traffic(), direction=ec2.TrafficDirection.EGRESS)

        # Associate NACL with subnets in prod_vpc
        for subnet in self.prod_vpc.public_subnets + self.prod_vpc.private_subnets:
            ec2.SubnetNetworkAclAssociation(self, f"ProdVpcNACLAssociation{subnet.node.id}", network_acl=prod_vpc_nacl, subnet=subnet)
        
        # Create NACL for mgmt_vpc
        mgmt_vpc_nacl = ec2.NetworkAcl(self, "MgmtVpcNACL", vpc=self.mgmt_vpc)

        # Add rules to allow inbound and outbound traffic from select IP addresses
        mgmt_vpc_nacl.add_entry("MgmtVpcInboundRule1", cidr=ec2.AclCidr.ipv4("82.75.30.6/32"), rule_number=200, traffic=ec2.AclTraffic.all_traffic(), direction=ec2.TrafficDirection.INGRESS)
        mgmt_vpc_nacl.add_entry("MgmtVpcOutboundRule1", cidr=ec2.AclCidr.ipv4("82.75.30.6/32"), rule_number=200, traffic=ec2.AclTraffic.all_traffic(), direction=ec2.TrafficDirection.EGRESS)

        # Add rules to allow inbound and outbound traffic between mgmt_vpc and prod_vpc
        mgmt_vpc_nacl.add_entry("MgmtVpcInboundRule2", cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block), rule_number=199, traffic=ec2.AclTraffic.all_traffic(), direction=ec2.TrafficDirection.INGRESS)
        mgmt_vpc_nacl.add_entry("MgmtVpcOutboundRule2", cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block), rule_number=199, traffic=ec2.AclTraffic.all_traffic(), direction=ec2.TrafficDirection.EGRESS)

        # Associate NACL with subnets in mgmt_vpc
        for subnet in self.mgmt_vpc.public_subnets:
            ec2.SubnetNetworkAclAssociation(self, f"MgmtVpcNACLAssociation{subnet.node.id}", network_acl=mgmt_vpc_nacl, subnet=subnet)
        '''
        
        
        # Fetching references to the subnets where we intend to deploy our servers
        self.subnet_webserver = self.prod_vpc.public_subnets[0]
        self.subnet_mgmtserver = self.mgmt_vpc.public_subnets[0]
       

    def setup_kms(self):
        # Create KMS Key for the management server
        '''self.kms_key = kms.Key(self, "KmsKey", removal_policy=cdk.RemovalPolicy.DESTROY)
        
        # Create an alias for the KMS key
        self.my_alias = kms.Alias(
            self,
            "MyAlias",
            alias_name="alias/PRO01CDK",
            target_key=self.kms_key
        )
        self.kms_key.add_to_resource_policy(
            iam.PolicyStatement(
                sid="Allow service-linked role use of the customer managed key",
                effect=iam.Effect.ALLOW,
                principals=[iam.ArnPrincipal(f"arn:aws:iam::{cdk.Aws.ACCOUNT_ID}:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling")],
                actions=[
                    "kms:Encrypt",
                    "kms:Decrypt",
                    "kms:ReEncrypt*",
                    "kms:GenerateDataKey*",
                    "kms:DescribeKey"
                ],
                resources=["*"]
            )
        )
        self.kms_key.add_to_resource_policy(
            iam.PolicyStatement(
                sid="Allow attachment of persistent resources",
                effect=iam.Effect.ALLOW,
                principals=[iam.ArnPrincipal(f"arn:aws:iam::{cdk.Aws.ACCOUNT_ID}:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling")],
                actions=[                    
                    "kms:ListGrants",
                    "kms:CreateGrant",
                    "kms:RevokeGrant",
                    "kms:ListRetirableGrants",
                    "kms:RetireGrant"
                ],
                resources=["*"],
                conditions={
                    "Bool": {
                        "kms:GrantIsForAWSResource": True
                    }
                }
            )
        )'''
        
        
                
    def setup_s3_bucket(self):
        # Create an S3 bucket for storing post deployment scripts
        self.bucket = s3.Bucket(self, "PostDeploymentScripts",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            bucket_name="postdeploymentscripts",
            encryption=s3.BucketEncryption.KMS,
            #encryption_key=self.kms_key  # Use KMS key for encryption
    )
        
    def setup_security_group(self):


        self.security_group_prod = ec2.SecurityGroup(
            self,
            "Security_Group_Prod",
            vpc=self.prod_vpc,
            allow_all_outbound=True,
        )

        self.security_group_mgmt = ec2.SecurityGroup(
            self,
            "Security_Group_Mgmt",
            vpc=self.mgmt_vpc,
            allow_all_outbound=True,
        )

        # Open port 80 (HTTP) on the security group for incoming traffic from any IP
        self.security_group_prod.connections.allow_from_any_ipv4(ec2.Port.tcp(80))

        # Open port 22 (SSH) on the security group for incoming traffic from any IP
        self.security_group_mgmt.connections.allow_from_any_ipv4(ec2.Port.tcp(22))

        # Open port 443 (HTTPS) on the security group for incoming traffic from any IP
        self.security_group_prod.connections.allow_from_any_ipv4(ec2.Port.tcp(443))
        
    # Create EC2 instances
    def setup_ec2(self):
        # Define AMI (Amazon Machine Image) for the EC2 instances
        '''self.amzn_linux_ami = ec2.AmazonLinuxImage(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
        )'''
        self.amzn_linux_ami = ec2.MachineImage.latest_amazon_linux2()
        ''' 
        # Create Web server 
        self.web_server = ec2.Instance(self, "Web_Server",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=self.amzn_linux_ami,
            key_name="exp3",
            vpc=self.prod_vpc,
            vpc_subnets=ec2.SubnetSelection(subnets=[self.subnet_webserver]),
            security_group=self.security_group_prod,
            user_data=ec2.UserData.custom('''#!/bin/bash
                # Install Apache Web Server and PHP 
        '''yum install -y httpd mysql php
                # Download Lab files
                wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
                unzip lab-app.zip -d /var/www/html/
                # Turn on web server
                chkconfig httpd on
                service httpd start''' '''),
            block_devices=[ec2.BlockDevice(
                device_name="/dev/xvda",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,
                    volume_type=ec2.EbsDeviceVolumeType.GP2,
                    encrypted=True
                    #kms_key=self.kms_key
                )
            )]
        )

        self.web_server.node.add_metadata("Name", "Web_Server")'''
        

        # Allocate an Elastic IP for the Web server
#        web_server_eip = ec2.CfnEIP(self, "WebServerEIP", instance_id=self.web_server.instance_id)
        
        # Create Management server
        self.mgmt_server = ec2.Instance(self, "Management_Server",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=self.amzn_linux_ami,
            vpc=self.mgmt_vpc,
            vpc_subnets=ec2.SubnetSelection(subnets=[self.subnet_mgmtserver]),
            security_group=self.security_group_mgmt,
            block_devices=[ec2.BlockDevice(
                device_name="/dev/xvda",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,
                    volume_type=ec2.EbsDeviceVolumeType.GP2,
                    encrypted=True,
                )
            )]
        )
        
        '''
        self.mgmt_server = ec2.BastionHostLinux(self, "BastionHost",
            vpc=self.mgmt_vpc,
            subnet_selection=ec2.SubnetSelection(subnets=[self.subnet_mgmtserver]),
            instance_name="BastionHost",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=self.amzn_linux_ami,
            security_group=self.security_group_mgmt,
            block_devices=[ec2.BlockDevice(
                device_name="/dev/xvda",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,
                    volume_type=ec2.EbsDeviceVolumeType.GP2,
                    encrypted=True,
                )
            )]
        )'''

        self.mgmt_server.node.add_metadata("Name", "Management_Server")

        

        # Allow SSH and RDP access from the management server to the production server
        # Allow inbound RDP traffic from the mgmt_server instance
        '''self.security_group_prod.add_ingress_rule(
            peer=ec2.Peer.ipv4(f"{self.mgmt_server.instance_public_ip}/32"),
            connection=ec2.Port.tcp(3389),
            description="Allow inbound RDP traffic from mgmt_server"
        )
    

        # Allow inbound SSH traffic from the mgmt_server instance
        self.security_group_prod.add_ingress_rule(
            peer=ec2.Peer.ipv4(f"{self.mgmt_server.instance_public_ip}/32"),
            connection=ec2.Port.tcp(22),
            description="Allow inbound SSH traffic from mgmt_server"
        )'''

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

    
        
    
    def setup_load_balancer(self):
        # Define a security group for the load balancer in the production VPC
        self.lb_security_group = ec2.SecurityGroup(
            self,
            "LBSecurityGroup",
            vpc=self.prod_vpc,
            description="Security Group for Load Balancer",
        )

        # Get the ID of the existing AMI
        web_server_image = ec2.MachineImage.generic_linux({
            self.region: "ami-0ed632c4c0afe9791" 
        })

        # Use the existing AMI when creating the AutoScalingGroup
        self.asg_web_server = autoscaling.AutoScalingGroup(
            self,
            "WebServerASG",
            vpc=self.prod_vpc,
            max_capacity=3,
            min_capacity=0,
            health_check=autoscaling.HealthCheck.elb(
                grace=cdk.Duration.minutes(5)
            ),
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=web_server_image, # Use the existing AMI
            key_name="exp3",
            security_group=self.security_group_prod,
            block_devices=[autoscaling.BlockDevice(
                device_name='/dev/xvda',
                volume=autoscaling.BlockDeviceVolume.ebs(
                    volume_size=8,
                    encrypted=True,
                )                
            )],
            associate_public_ip_address=False
        )

        
        # Create an application load balancer in a VPC
        self.lb = elbv2.ApplicationLoadBalancer(
            self,
            "LB",
            vpc=self.prod_vpc,
            internet_facing=True, # This makes the load balancer publicly accessible
            security_group=self.lb_security_group,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )
        # Add a listener to the load balancer on port 80
        listener = self.lb.add_listener(
            "Listener",
            port=80,
            open=True,  # Allows connections from any IP
        )
        
        # Configure the HTTP listener to redirect requests to HTTPS
        listener.add_action(
            "HTTPSRedirect",
            action=elbv2.ListenerAction.redirect(
                protocol="HTTPS",
                port="443",
                host="#{host}",
                path="/#{path}",
                query="#{query}",
            ),
        )
        
        # Import an existing SSL certificate
        certificate = acm.Certificate.from_certificate_arn(
            self,
            "Certificate",
            certificate_arn="arn:aws:acm:eu-central-1:989030117675:certificate/d98550cd-f194-43fb-ac7b-0ebb571be024",
        )

        # Add an HTTPS listener
        https_listener = self.lb.add_listener(
            "HTTPSListener",
            port=443,
            protocol=elbv2.ApplicationProtocol.HTTPS,
            certificates=[certificate],
        )
        
        # Create a target group for the web servers
        self.web_server_target_group = elbv2.ApplicationTargetGroup(
            self,
            "WebServerTargetGroup",
            vpc=self.prod_vpc,
            port=80,
            protocol=elbv2.ApplicationProtocol.HTTP,
            targets=[self.asg_web_server]
        )
        
        # Add a default action to the HTTPS listener
        https_listener.add_action(
            "DefaultAction",
            action=elbv2.ListenerAction.forward(
                target_groups=[self.web_server_target_group],
            ),
        )

        self.web_server_target_group.configure_health_check(
            interval=cdk.Duration.seconds(60),
            path="/",
            timeout=cdk.Duration.seconds(5)
        )
        ''' 
        with open('certificate.pem', 'r') as file:
            certificate_body = file.read()

        with open('privatekey.pem', 'r') as file:
            private_key = file.read()

        certificate = acm.Certificate.from_certificate_arn(
            self,
            "Certificate",
            certificate_arn=acm.Certificate.from_certificate_pem(
                self,
                "ImportedCertificate",
                certificate_body=certificate_body,
                private_key=private_key
            ).certificate_arn
        )'''
        '''
        # Create an AutoScaling group and add the web server as a target
        listener.add_targets(
            "WebServerTarget",
            targets=[self.asg_web_server],
            port=80,
            health_check=elbv2.HealthCheck(
                interval=cdk.Duration.seconds(60),
                path="/",  # Path for the load balancer to check (e.g., the root path of your website)
                timeout=cdk.Duration.seconds(5)  # The amount of time to wait when receiving a response from the health check
            ),
        )'''
        
        
        # Create a custom metric for CPU utilization
        cpu_metric = cloudwatch.Metric(
            namespace="AWS/EC2",
            metric_name="CPUUtilization",
            dimensions_map={"AutoScalingGroupName": self.asg_web_server.auto_scaling_group_name},
            statistic="Average",
        )

        # Create a step scaling policy
        step_scaling_policy = autoscaling.StepScalingPolicy(
            self,
            "StepScalingPolicy",
            auto_scaling_group=self.asg_web_server,
            metric=cpu_metric,
            adjustment_type=autoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
            scaling_steps=[
                autoscaling.ScalingInterval(lower=0, upper=40, change=-1),
                autoscaling.ScalingInterval(lower=70, change=1),
            ],
        )

        self.security_group_prod.connections.allow_from(self.lb_security_group, ec2.Port.tcp(80))
        self.security_group_prod.connections.allow_from(self.lb_security_group, ec2.Port.tcp(443))

        




    # Setup AWS Backup to backup all VM disks from both VPC's daily, and retain them for a period of 7 days 
    def setup_backup(self):

        # Define a role for the backup 
        backup_role = iam.Role(self, "BackupRole",
                            assumed_by=iam.ServicePrincipal("backup.amazonaws.com"))

        # Define the ARN of your KMS key
        #kms_key_arn = "arn:aws:kms:REGION:ACCOUNT_ID:key/KMS_KEY_ID"  # Replace with the ARN of your KMS key

        # Create a new policy that grants access to perform backups
        backup_policy = iam.Policy(self, "BackupPolicy",
            policy_name="backup-policy",
            statements=[
                iam.PolicyStatement(
                    actions=[
                        "backup:StartBackupJob",
                        "backup:StopBackupJob",
                        "backup:DescribeBackupJob",
                        "backup:ListBackupJobs",
                        "backup:StartCopyJob",
                        "backup:DescribeCopyJob",
                        "backup:ListCopyJobs",
                        "backup:DescribeBackupVault",
                        "backup:CopyIntoBackupVault"
                    ],
                    resources=["*"],
                    effect=iam.Effect.ALLOW,
                    sid="AWSBackupPermissions"
                ),
            iam.PolicyStatement(
                actions=[
                    "ec2:DescribeInstances",
                    "ec2:DescribeVolumes",
                    "ec2:DescribeSnapshots",
                    "ec2:DescribeInstanceAttribute",
                    "ec2:DescribeInstanceStatus",
                    "ec2:CreateTags",
                    'ec2:CreateSnapshot',
                    "ec2:DeleteSnapshot",
                    "ec2:CreateImage",
                    "ec2:DeregisterImage",
                    "ec2:CopyImage",
                    "ec2:CopySnapshot",
                    "ec2:CreateTags",
                    "ec2:DescribeSnapshots",
                    "ec2:DescribeTags",
                    "ec2:DescribeImages",
                    "ec2:DescribeInstanceCreditSpecifications",
                    "ec2:DescribeNetworkInterfaces",
                    "ec2:DescribeElasticGpus",
                    "ec2:DescribeSpotInstanceRequests",
                    "tag:GetResources"
                ],
                resources=["*"],
                effect=iam.Effect.ALLOW,
                sid="EC2BackupPermissions"
            ),
            iam.PolicyStatement(
                actions=[
                    "s3:GetObject",
                    "s3:GetObjectVersion",
                    "s3:GetObjectVersionTagging",
                    "s3:GetObjectVersionAcl",
                    "s3:GetBucketLocation",
                    "s3:GetInventoryConfiguration",
                    "s3:PutInventoryConfiguration",
                    's3:ListBucket',
                    "s3:ListBucketVersions",
                    "s3:GetBucketVersioning",
                    "s3:GetBucketNotification",
                    "s3:PutBucketNotification",
                    "s3:GetBucketTagging",
                    "s3:GetBucketAcl",
                    "s3:GetObjectAcl",
                    "s3:GetObjectTagging",
                    "s3:ListAllMyBuckets"
                ],
                resources=["*"],
                effect=iam.Effect.ALLOW,
                sid="S3BucketBackupPermissions"
            ),
            iam.PolicyStatement(
                actions=[
                    'kms:Encrypt',
                    'kms:Decrypt',
                    'kms:ReEncrypt*',
                    'kms:GenerateDataKey*',
                    'kms:DescribeKey'
                ],
                resources=['*'],
                #resources=[self.kms_key.key_arn],
                effect=iam.Effect.ALLOW,
                sid="KMSPermissions",
                conditions={"StringLike": {"kms:ViaService": "s3.*.amazonaws.com"}}
            ),
            iam.PolicyStatement(
                actions=[
                    'cloudwatch:GetMetricData',
                    "events:ListRules"
                ],
                resources=['*'],
                effect=iam.Effect.ALLOW,
                sid="EventsMetricsGlobalPermissions"
            ),
            iam.PolicyStatement(
                actions=[
                    "events:DescribeRule",
                    "events:EnableRule",
                    "events:PutRule",
                    "events:DeleteRule",
                    "events:PutTargets",
                    "events:RemoveTargets",
                    "events:ListTargetsByRule",
                    "events:DisableRule",
                ],
                resources=["arn:aws:events:*:*:rule/AwsBackupManagedRule*"], 
                effect=iam.Effect.ALLOW,
                sid="EventsPermissions"
            ),
            iam.PolicyStatement(
                actions=[
                    "rds:AddTagsToResource",
                    "rds:ListTagsForResource",
                    "rds:DescribeDBSnapshots",
                    "rds:CreateDBSnapshot",
                    "rds:CopyDBSnapshot",
                    "rds:DescribeDBInstances",
                    "rds:CreateDBClusterSnapshot",
                    "rds:DescribeDBClusters",
                    "rds:DescribeDBClusterSnapshots",
                    "rds:CopyDBClusterSnapshot"
                ],
                resources=["*"],
                effect=iam.Effect.ALLOW,
                sid="RDSGeneralBackupPermissions"
            ),
            iam.PolicyStatement(
                actions=[
                    "rds:DeleteDBSnapshot",
                    "rds:ModifyDBSnapshotAttribute"
                ],
                resources=[
                    "arn:aws:rds:*:*:snapshot:awsbackup:*"
                ],
                effect=iam.Effect.ALLOW,
                sid="RDSSnapshotBackupPermissions"
            ),
            iam.PolicyStatement(
                actions=[
                    "rds:DeleteDBClusterSnapshot",
                    "rds:ModifyDBClusterSnapshotAttribute"
                ],
                resources=[
                    "arn:aws:rds:*:*:cluster-snapshot:awsbackup:*"
                ],
                effect=iam.Effect.ALLOW,
                sid="RDSClusterSnapshotBackupPermissions"
            ),
            iam.PolicyStatement(
                actions=[
                    "tag:GetResources"
                ],
                resources=["*"],
                effect=iam.Effect.ALLOW,
                sid="RDSTagResourcesPermissions"
            ),
            iam.PolicyStatement(
                actions=[
                    "backup:DescribeBackupVault",
                    "backup:CopyIntoBackupVault"
                ],
                resources=["arn:aws:backup:*:*:backup-vault:*"],
                effect=iam.Effect.ALLOW,
                sid="RDSBackupVaultPermissions"
            ),
            iam.PolicyStatement(
                actions=["kms:DescribeKey"],
                resources=["*"],
                effect=iam.Effect.ALLOW,
                sid="RDSKMSPermissions"
            ),
            
        ]
    )
        
    

        # Attach the policy to the IAM role
        backup_policy.attach_to_role(backup_role)

        # Create a new backup vault
        backup_vault = backup.BackupVault(
            self,
            "my-backup-vault",
            backup_vault_name="my-backup-vault",
            #encryption_key=self.kms_key,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )

        # Create a new backup plan
        backup_plan = backup.CfnBackupPlan(
            self,
            "BackupPlan",
            backup_plan=backup.CfnBackupPlan.BackupPlanResourceTypeProperty(
                backup_plan_name="my-backup-plan",
                backup_plan_rule=[
                    backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                        rule_name="my-backup-rule",
                        target_backup_vault=backup_vault.backup_vault_name,
                        completion_window_minutes=120,
                        schedule_expression="cron(0 12 * * ? *)",
                        start_window_minutes=60,
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=7
                        ),                
                    ),
                ],
            ),
        )

        # Create a new backup selection
        backup_selection = backup.CfnBackupSelection(
            self,
            "BackupSelection",
            backup_plan_id=backup_plan.ref,
            backup_selection=backup.CfnBackupSelection.BackupSelectionResourceTypeProperty(
                iam_role_arn=backup_role.role_arn,  # Use the ARN of the backup_role
                selection_name="my-backup-selection",
                resources=[
                    #f"arn:aws:ec2:{self.region}:{self.account}:instance/{self.web_server.instance_id}",  # Reference to the web server instance
                    f"arn:aws:ec2:{self.region}:{self.account}:instance/{self.mgmt_server.instance_id}",  # Reference to the management server instance
                    self.bucket.bucket_arn,  # Reference to the S3 bucket
                   # f"arn:aws:rds:{self.region}:{self.account}:db:my-rds-instance",  # Reference to the RDS instance
                ],
            ),
        )
    
    def setup_db(self):
        

        ''' # Low-level constructs code
                

        db_security_group = ec2.SecurityGroup(
            self, 
            "DBSecurityGroup",
            vpc=self.prod_vpc,
            description="Allow connections to database",
            allow_all_outbound=True
        )

        # Allow inbound traffic on default mysql port
        
        self.security_group_prod.connections.allow_from(
            self.security_group_prod, 
            ec2.Port.tcp(3306), 
        )'''

        
        
        # High-level constructs code
        '''subnet_group = rds.SubnetGroup(
            self,
            "myDBSubnetGroup",
            description="Subnets available for the RDS DB Instance",
            vpc=self.prod_vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
        )

        db_security_group = ec2.SecurityGroup(
            self,
            "DBSecurityGroup",
            vpc=self.prod_vpc,
            description="Allow connections to database",
            allow_all_outbound=True,
        )

        # Allow inbound traffic on default mysql port
        db_security_group.add_ingress_rule(
            ec2.Peer.ipv4(self.prod_vpc.vpc_cidr_block),
            ec2.Port.tcp(3306),
        )

        # Create RDS instance in vpc2
        self.db_instance = rds.DatabaseInstance(
            self,
            "RDSInstance",
            database_name="database1",
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0
            ),
            instance_type=ec2.InstanceType("t3.micro"),
            vpc=self.prod_vpc,
            security_groups=[db_security_group],
            subnet_group=subnet_group,
            publicly_accessible=False,
            storage_encrypted=True,
            #storage_encryption_key=self.kms_key,
            auto_minor_version_upgrade=True,
            backup_retention=cdk.Duration.days(7),
            multi_az=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )'''
        
                # Peering Stack
    def setup_peering(self):

        
        self.peering_stack = NetworkPeeringStack(
            self,
            "NetworkPeeringStack",
            vpc_one=self.prod_vpc,
            vpc_two=self.mgmt_vpc,
        )
        
    
class NetworkPeeringStack(NestedStack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc_one: ec2.Vpc,
        vpc_two: ec2.Vpc,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)


        
        # Peering connection
        self.vpc1tovpc2 = ec2.CfnVPCPeeringConnection(
            self,
            "vpc1tovpc2",
            vpc_id=vpc_one.vpc_id,
            peer_vpc_id=vpc_two.vpc_id,
        )
        '''
        # Check status of VPC peering connection
        cr.AwsCustomResource(
            self,
            "CheckVpcPeeringConnectionStatus",
            policy=cr.AwsCustomResourcePolicy.from_sdk_calls(resources=cr.AwsCustomResourcePolicy.ANY_RESOURCE),
            on_create=cr.AwsSdkCall(
                service="EC2",
                action="describeVpcPeeringConnections",
                parameters={"VpcPeeringConnectionIds": [self.vpc1tovpc2.ref]},
                physical_resource_id=cr.PhysicalResourceId.of("CheckVpcPeeringConnectionStatus"),
            ),
            on_update=cr.AwsSdkCall(
                service="EC2",
                action="describeVpcPeeringConnections",
                parameters={"VpcPeeringConnectionIds": [self.vpc1tovpc2.ref]},
                physical_resource_id=cr.PhysicalResourceId.of("CheckVpcPeeringConnectionStatus"),
            ),
        )
        '''
        '''
        ec2.CfnRoute(
            self,
            "RouteFromVPC1toVPC2",
            destination_cidr_block=vpc_two.vpc_cidr_block,
            route_table_id=vpc_one.public_subnets[0].route_table.route_table_id,
            vpc_peering_connection_id=self.vpc1tovpc2.ref,
        )

        ec2.CfnRoute(
            self,
            "RouteFromVPC2toVPC1",
            destination_cidr_block=vpc_one.vpc_cidr_block,
            route_table_id=vpc_two.public_subnets[0].route_table.route_table_id,
            vpc_peering_connection_id=self.vpc1tovpc2.ref,
        )
        '''

        # Add routes to all subnets in VPC one
        for subnet in vpc_one.select_subnets().subnets:
            ec2.CfnRoute(
                self,
                f"RouteFromVPC1toVPC2-{subnet.node.id}",
                destination_cidr_block=vpc_two.vpc_cidr_block,
                route_table_id=subnet.route_table.route_table_id,
                vpc_peering_connection_id=self.vpc1tovpc2.ref,
            )
        
        # Add routes to all public subnets in VPC one
        for subnet in vpc_one.public_subnets:
            ec2.CfnRoute(
                self,
                f"RouteFromVPC1toVPC2-{subnet.node.id}",
                destination_cidr_block=vpc_two.vpc_cidr_block,
                route_table_id=subnet.route_table.route_table_id,
                vpc_peering_connection_id=self.vpc1tovpc2.ref,
            )
        
        '''# Add routes to all private subnets in VPC one
        for subnet in vpc_one.private_subnets:
            ec2.CfnRoute(
                self,
                f"RouteFromVPC1toVPC2-{subnet.node.id}",
                destination_cidr_block=vpc_two.vpc_cidr_block,
                route_table_id=subnet.route_table.route_table_id,
                vpc_peering_connection_id=self.vpc1tovpc2.ref,
            )'''
        
        # Add routes to all public subnets in VPC two
        '''for subnet in vpc_two.public_subnets:
            ec2.CfnRoute(
                self,
                f"RouteFromVPC2toVPC1-{subnet.node.id}",
                destination_cidr_block=vpc_one.vpc_cidr_block,
                route_table_id=subnet.route_table.route_table_id,
                vpc_peering_connection_id=self.vpc1tovpc2.ref,
            )

            # Add routes to all subnets in VPC two
        for subnet in vpc_two.select_subnets().subnets:
            ec2.CfnRoute(
                self,
                f"RouteFromVPC2toVPC1-{subnet.node.id}",
                destination_cidr_block=vpc_one.vpc_cidr_block,
                route_table_id=subnet.route_table.route_table_id,
                vpc_peering_connection_id=self.vpc1tovpc2.ref,
            )'''

        
        '''self.vpc1tovpc2 = ec2.VpcPeeringConnection(
            self,
            "vpc1tovpc2",
            vpc=vpc_one,
            peer_vpc=vpc_two,
        )'''

        '''# Add routes to all subnets in VPC one
        for subnet in vpc_one.select_subnets().subnets:
            subnet.add_route(
                f"RouteFromVPC1toVPC2-{subnet.node.id}",
                destination_cidr_block="10.20.20.0/24",
                router_type=ec2.RouterType.VPC_PEERING_CONNECTION,
                router_id=self.vpc1tovpc2.ref,
            )'''

        '''route_id = 0
        for vpc_subnet in vpc_one.public_subnets:
            route_id += 1

            ec2.CfnRoute(
                self,
                f"PeeringRouteNumber{route_id}",
                destination_cidr_block=vpc_two.vpc_cidr_block,
                route_table_id=vpc_subnet.route_table.route_table_id,
                vpc_peering_connection_id=self.vpc1tovpc2.ref,
            )'''

        # Add routes to all subnets in VPC two
        for subnet in vpc_two.select_subnets().subnets:
            subnet.add_route(
                f"RouteFromVPC2toVPC1-{subnet.node.id}",
                destination_cidr_block="10.10.10.0/24",
                router_type=ec2.RouterType.VPC_PEERING_CONNECTION,
                router_id=self.vpc1tovpc2.ref,
            )


