from aws_cdk import NestedStack, Stack, aws_ec2 as ec2, aws_rds as rds, aws_s3 as s3
from constructs import Construct
import aws_cdk as cdk
from aws_cdk import aws_elasticloadbalancingv2 as elbv2, aws_autoscaling as autoscaling
from aws_cdk import aws_events as events, aws_events_targets as targets
from aws_cdk import aws_backup as backup
from aws_cdk import aws_iam as iam
from aws_cdk import aws_autoscaling_common as common
from aws_cdk import aws_cloudwatch as cloudwatch
from aws_cdk import aws_certificatemanager as acm
from aws_cdk import aws_s3_deployment as s3deploy
from aws_cdk import aws_sqs as sqs
from aws_cdk import aws_secretsmanager as secretsmanager
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_event_sources as lambda_sources
import json


class Pro11CdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.setup_vpc()
        self.setup_peering()
        self.setup_security_group()
        self.setup_ec2()
        self.setup_s3_bucket()
        self.setup_load_balancer()
        self.setup_secrets()
        self.setup_db()
        self.setup_backup()
        self.setup_lambda()

    def setup_vpc(self):    
        # Public - NAT
        self.prod_vpc = ec2.Vpc(
            self,
            "Production Network",
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
            gateway_endpoints={
                "S3": ec2.GatewayVpcEndpointOptions(
                    service=ec2.GatewayVpcEndpointAwsService.S3
                )
            },
        )

        
        self.mgmt_vpc = ec2.Vpc(
            self,
            "Management Network",
            ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public Subnet"                    
                ),                
            ],
            availability_zones=["eu-central-1a", "eu-central-1b"],            
        )
        
        # Create a new NACL for the public subnets of prod_vpc
        self.prod_public_nacl = ec2.NetworkAcl(
            self,
            "ProdPublicNACL",
            vpc=self.prod_vpc,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

        # Allow inbound traffic from ephemeral ports
        self.prod_public_nacl.add_entry(
            "Allow Ephemeral Ports",
            cidr=ec2.AclCidr.ipv4("0.0.0.0/0"),
            rule_number=105,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
        )

        # Allow inbound HTTP traffic from anywhere
        self.prod_public_nacl.add_entry(
            "Allow HTTP",
            cidr=ec2.AclCidr.ipv4("0.0.0.0/0"),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port_range(80, 80),
            direction=ec2.TrafficDirection.INGRESS,
        )

        # Allow inbound HTTPS traffic from anywhere
        self.prod_public_nacl.add_entry(
            "Allow HTTPS",
            cidr=ec2.AclCidr.ipv4("0.0.0.0/0"),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(443, 443),
            direction=ec2.TrafficDirection.INGRESS,
        )

        # Allow inbound traffic from the mgmt_vpc
        self.prod_public_nacl.add_entry(
            "Allow Mgmt VPC",
            cidr=ec2.AclCidr.ipv4(self.mgmt_vpc.vpc_cidr_block),
            rule_number=130,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.INGRESS,
        )

        # Allow inbound traffic from private NACL to public NACL
        self.prod_public_nacl.add_entry(
            "AllowInboundFromPublicNACL",
            cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.INGRESS
        )

        # Allow all outbound traffic
        self.prod_public_nacl.add_entry(
            "Allow All Outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS,
        )

        # Create a new NACL for the private subnets of prod_vpc
        self.prod_private_nacl = ec2.NetworkAcl(
            self,
            "ProdPrivateNACL",
            vpc=self.prod_vpc,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
        )

        self.prod_private_nacl.add_entry(
            "Allow RDP traffic Inbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=101,
            traffic=ec2.AclTraffic.tcp_port_range(3306, 3306),
            direction=ec2.TrafficDirection.INGRESS,
        )

        # Allow inbound traffic from the RDS instance to the private subnets of prod_vpc
        self.prod_private_nacl.add_entry(
            "Allow RDS",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=105,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
        )

        # Allow inbound traffic from public NACL to private NACL
        self.prod_private_nacl.add_entry(
            "AllowInboundFromPublicNACL",
            cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block),
            rule_number=102,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.INGRESS
        )



        # Allow inbound traffic from the mgmt_vpc
        self.prod_private_nacl.add_entry(
            "Allow Mgmt VPC",
            cidr=ec2.AclCidr.ipv4(self.mgmt_vpc.vpc_cidr_block),
            rule_number=109,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.INGRESS,
        )

        # Allow all outbound traffic
        self.prod_private_nacl.add_entry(
            "Allow All Outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS,
        )

        # Create a new NACL for the public subnets of mgmt_vpc
        self.mgmt_public_nacl = ec2.NetworkAcl(
            self,
            "MgmtPublicNACL",
            vpc=self.mgmt_vpc,
            subnet_selection=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
        )

        

        # Add rules to allow inbound traffic from select IP addresses
        self.ip_address = self.node.try_get_context("ip_address")
        self.mgmt_public_nacl.add_entry(
            "Allow IP Admin",
            cidr=ec2.AclCidr.ipv4(self.ip_address),
            rule_number=200,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.INGRESS,
        )

        # Add rules to allow inbound between mgmt_vpc and prod_vpc
        self.mgmt_public_nacl.add_entry(
            "Allow Prod VPC",
            cidr=ec2.AclCidr.ipv4(self.prod_vpc.vpc_cidr_block),
            rule_number=199,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.INGRESS,
        )
        # Allow all outbound traffic
        self.mgmt_public_nacl.add_entry(
            "Allow All Outbound",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.all_traffic(),
            direction=ec2.TrafficDirection.EGRESS,
        )

    def setup_s3_bucket(self):

        # Create an S3 bucket for storing post deployment scripts
        self.bucket = s3.Bucket(self, "PostDeploymentScripts",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            bucket_name="postdeploymentscripts",
            encryption=s3.BucketEncryption.KMS,
        )

        s3deploy.BucketDeployment(self, 'DeployFile',
            sources=[s3deploy.Source.asset('./mysqlsampledatabase.zip')],
            destination_bucket=self.bucket
        )

        # Create an interface endpoint for S3
        s3_interface_endpoint = ec2.InterfaceVpcEndpoint(
            self,
            "S3InterfaceEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.S3,
            vpc=self.prod_vpc,
            subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            private_dns_enabled=False,
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


        ## Production VPC Security Groups
        # Open port 80 (HTTP) on the security group for incoming traffic from any IP
        self.security_group_prod.connections.allow_from_any_ipv4(ec2.Port.tcp(80))

        # Open port 443 (HTTPS) on the security group for incoming traffic from any IP
        self.security_group_prod.connections.allow_from_any_ipv4(ec2.Port.tcp(443))


        ## Management VPC Security Groups

        # Open port 80 (HTTP) on the security group for incoming traffic from any IP
        self.security_group_mgmt.connections.allow_from_any_ipv4(ec2.Port.tcp(80))

        # Open port 443 (HTTPS) on the security group for incoming traffic from any IP
        self.security_group_mgmt.connections.allow_from_any_ipv4(ec2.Port.tcp(443))

        # Open port 22 (SSH) on the security group for incoming traffic from the specified IP
        self.security_group_mgmt.connections.allow_from(ec2.Peer.ipv4(self.ip_address), ec2.Port.tcp(22))

        # Open port 3389 (RDP) on the security group for incoming traffic from the specified IP
        self.security_group_mgmt.connections.allow_from(ec2.Peer.ipv4(self.ip_address), ec2.Port.tcp(3389))



        
    # Create EC2 instances
    def setup_ec2(self):
        # Define AMI (Amazon Machine Image) for the EC2 instances

        

        # Get the ID of the existing AMI
        self.mgmt_server_image = ec2.MachineImage.generic_windows({
        self.region:"ami-0f7780b59d41b6e19" 
        })
        
        self.mgmt_server = ec2.Instance(
            self,
            "Management_Server",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=self.mgmt_server_image,
            vpc=self.mgmt_vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=self.security_group_mgmt,
            key_name="exp3",
            #user_data=user_data,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=32,
                        volume_type=ec2.EbsDeviceVolumeType.GP2,
                        encrypted=True,
                    ),
                )
            ],
        )        

        self.mgmt_server.node.add_metadata("Name", "Management_Server")

        

        # Allow SSH and RDP access from the management server to the production server


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
            self.region: "ami-056b1a787955b2bb6" 
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
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
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
            ssl_policy=elbv2.SslPolicy.TLS12_EXT # Only allow TLS 1.2 or higher
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
                    f"arn:aws:ec2:{self.region}:{self.account}:instance/{self.mgmt_server.instance_id}",  # Reference to the management server instance
                    self.bucket.bucket_arn,  # Reference to the S3 bucket
                ],
            ),
        )

    def setup_secrets(self):
    # Create a secret to store the database password
        self.db_secret = secretsmanager.Secret(
            self,
            "DBSecret",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template=json.dumps({"username": "admin"}),
                generate_string_key="password",
                exclude_characters='"@/\\',
            ),
        )

        # Create a VPC endpoint for Secrets Manager
        secretsmanager_endpoint = self.prod_vpc.add_interface_endpoint(
            "SecretsManagerEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.SECRETS_MANAGER,
        )

    def setup_db(self):
        
        
        # High-level constructs code
        subnet_group = rds.SubnetGroup(
            self,
            "myDBSubnetGroup",
            description="Subnets available for the RDS DB Instance",
            vpc=self.prod_vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
        )

        self.db_security_group = ec2.SecurityGroup(
            self,
            "DBSecurityGroup",
            vpc=self.prod_vpc,
            description="Allow connections to database",
            allow_all_outbound=True,
        )

        # Create RDS instance in vpc2
        self.db_instance = rds.DatabaseInstance(
            self,
            "MySQLForLambda",
            database_name="ExampleDB",
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0
            ),
            instance_type=ec2.InstanceType("t3.micro"),
            vpc=self.prod_vpc,
            security_groups=[self.db_security_group],
            subnet_group=subnet_group,
            publicly_accessible=False,
            storage_encrypted=True,
            auto_minor_version_upgrade=True,
            backup_retention=cdk.Duration.days(7),
            multi_az=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            credentials=rds.Credentials.from_secret(self.db_secret),
            )
        
        self.db_security_group.connections.allow_from(
            self.security_group_prod, ec2.Port.tcp(3306)
            )
        self.security_group_prod.connections.allow_from(
            self.db_security_group, ec2.Port.tcp(3306)
            )
        self.security_group_mgmt.connections.allow_from(
            self.db_security_group, ec2.Port.tcp(3306)
            )
        self.db_security_group.connections.allow_from(
            self.security_group_mgmt, ec2.Port.tcp(3306)
            )
        

    def setup_lambda(self):


        # Define a parameter to accept the secret ARN as input
        
        secret = secretsmanager.Secret(self, "Secret")


        # Create an IAM role for your Lambda function with necessary permissions
        role = iam.Role(
            self,
            "lambda-vpc-sqs-role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaVPCAccessExecutionRole"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaSQSQueueExecutionRole"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"))
        # Add a policy statement to allow the GetSecretValue action on the DBSecret resource
        role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["secretsmanager:DescribeSecret","secretsmanager:GetSecretValue"],
            resources=[self.db_secret.secret_arn],
        ))

        
        # Get a reference to the KMS key that was automatically created for the bucket
        my_key = self.bucket.encryption_key

        # Add a policy statement to your lambda function's IAM role to allow it to use the KMS key
        role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["kms:Decrypt"],
            resources=[my_key.key_arn],
        ))

         # Create a security group for the Lambda function
        self.lambda_sg = ec2.SecurityGroup(self, "LambdaSG",
            vpc=self.prod_vpc,
            description="Security group for Lambda function"
        )

        # Create a Lambda function that uses the code from your .zip deployment package
        function = _lambda.Function(
            self,
            "LambdaFunctionWithRDS",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda_function.zip"),
            role=role,
            vpc=self.prod_vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            security_groups=[self.lambda_sg],
            timeout=cdk.Duration.seconds(30),
            environment={
                "USER_NAME": "admin",
                "RDS_HOST": self.db_instance.db_instance_endpoint_address,
                "DB_NAME": "ExampleDB",
                "SECRET_NAME": self.db_secret.secret_name 
            },
        )

        self.db_security_group.connections.allow_from(
            self.lambda_sg, ec2.Port.tcp(3306)
            )

        secret.grant_read(function)

        # Create an Amazon SQS queue and configure it to invoke your Lambda function whenever a new message is added.
        queue = sqs.Queue(self, "LambdaRDSQueue")
        function.add_event_source(lambda_sources.SqsEventSource(queue))

        
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

        # Add routes to all public subnets in VPC two
        for subnet in vpc_two.public_subnets:
            ec2.CfnRoute(
                self,
                f"RouteFromVPC2toVPC1-{subnet.node.id}",
                destination_cidr_block=vpc_one.vpc_cidr_block,
                route_table_id=subnet.route_table.route_table_id,
                vpc_peering_connection_id=self.vpc1tovpc2.ref,
            )



