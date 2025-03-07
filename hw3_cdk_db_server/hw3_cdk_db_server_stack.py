from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_rds as rds,
    Stack
)
from constructs import Construct

class Hw3CdkDbServerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, cdk_db_vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        #First, definign instance role for Ec2 instances
        
        InstanceRole = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        InstanceRole.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))
        
        #Next, defining the two VPC's in the public subnets created by network_stack
        db_ec2_01 = ec2.Instance(self, "hw3_lab_instance1", vpc=cdk_db_vpc,
                                            instance_type=ec2.InstanceType("t2.micro"),
                                            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                                            role=InstanceRole,
                                            vpc_subnets = ec2.SubnetSelection(
                                                subnets = [cdk_db_vpc.public_subnets[0]]
                                            ) 
                                            
        )
        
        
        db_ec2_02 = ec2.Instance(self, "hw3_lab_instance2", vpc=cdk_db_vpc,
                                            instance_type=ec2.InstanceType("t2.micro"),
                                            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                                            role=InstanceRole,
                                            vpc_subnets = ec2.SubnetSelection(
                                                subnets = [cdk_db_vpc.public_subnets[1]]
                                            )
        )
        
        #Configuring db_ec2 instances to allow incoming traffic from port 80 (all)
        db_ec2_01.connections.allow_from_any_ipv4(ec2.Port.tcp(80))
        db_ec2_02.connections.allow_from_any_ipv4(ec2.Port.tcp(80))
        
        #Setting up RDS resource in the private subnets of the VPC
        db_rds = rds.DatabaseInstance(self, "hw3_lab_rds", vpc = cdk_db_vpc,
                     engine = rds.DatabaseInstanceEngine.MYSQL,
                     port = 3306,
                     vpc_subnets = ec2.SubnetSelection(
                         subnets = [cdk_db_vpc.private_subnets[0],cdk_db_vpc.private_subnets[1]]
                     )
        )
        
        db_rds.connections.allow_from(
            db_ec2_01,
            ec2.Port.tcp(3306),
            "Allows rds to connect to Instance in subnet1 over 3306"
        )
        
        db_rds.connections.allow_from(
            db_ec2_02,
            ec2.Port.tcp(3306),
            "Allows rds to connect to Instance in subnet2 over 3306"
        )
        
        