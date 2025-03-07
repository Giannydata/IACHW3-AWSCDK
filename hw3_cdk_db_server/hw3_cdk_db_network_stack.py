from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class Hw3CdkDbNetworkStack(Stack):
    
    @property
    def vpc(self):
        return self.cdk_db_vpc

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        self.cdk_db_vpc = ec2.Vpc(
            self, "cdk_db_vpc",
            ip_addresses = ec2.IpAddresses.cidr("10.0.0.0/16"),
            subnet_configuration = [
                ec2.SubnetConfiguration(name="PublicSubnet", subnet_type = ec2.SubnetType.PUBLIC, cidr_mask=24),
                ec2.SubnetConfiguration(name="PrivateSubnet1", subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS, cidr_mask=24)
                ]
        )

        
        
        