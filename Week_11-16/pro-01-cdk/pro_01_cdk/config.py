from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm
)
# basic VPC configs
VPC = 'custom-vpc'


INTERNET_GATEWAY_1 = 'internet-gateway-1'
INTERNET_GATEWAY_2 = 'internet-gateway-2'
NAT_GATEWAY = 'nat-gateway'
REGION = 'eu-central-1'

# route tables
PUBLIC_ROUTE_TABLE_1 = 'public-route-table-1'
PUBLIC_ROUTE_TABLE_2 = 'public-route-table-2'


ROUTE_TABLES_ID_TO_ROUTES_MAP_1 = {
    PUBLIC_ROUTE_TABLE_1: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY_1,
            'router_type': ec2.RouterType.GATEWAY
        }
    ]
}

ROUTE_TABLES_ID_TO_ROUTES_MAP_2 = {
        PUBLIC_ROUTE_TABLE_2: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY_2,
            'router_type': ec2.RouterType.GATEWAY
        }
    ]
}

# subnets and instances
PUBLIC_SUBNET_1 = 'public-subnet-1'
PUBLIC_SUBNET_2 = 'public-subnet-2'
PUBLIC_SUBNET_3 = 'public-subnet-3'
PUBLIC_SUBNET_4 = 'public-subnet-4'


PUBLIC_INSTANCE = 'public-instance'

SUBNET_CONFIGURATION_1 = {
    PUBLIC_SUBNET_1: {
        'availability_zone': 'eu-central-1a',
        'cidr_block': '10.10.10.0/25',
        'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE_1,
    },
    PUBLIC_SUBNET_2: {
        'availability_zone': 'eu-central-1b',
        'cidr_block': '10.10.10.128/25',
        'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE_1,
    }
}

SUBNET_CONFIGURATION_2 = {
    PUBLIC_SUBNET_3: {
        'availability_zone': 'eu-central-1a',
        'cidr_block': '10.20.20.0/25',
        'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE_2,
    },
    PUBLIC_SUBNET_4: {
        'availability_zone': 'eu-central-1b',
        'cidr_block': '10.20.20.128/25',
        'map_public_ip_on_launch': True,
        'route_table_id': PUBLIC_ROUTE_TABLE_2,
    }
}