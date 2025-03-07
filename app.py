#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hw3_cdk_db_server.hw3_cdk_db_server_stack import Hw3CdkDbServerStack
from hw3_cdk_db_server.hw3_cdk_db_network_stack import Hw3CdkDbNetworkStack


app = cdk.App()

NetworkStack = Hw3CdkDbNetworkStack(app, "CdkDbNetworkStack")
Hw3CdkDbServerStack(app, "Hw3CdkDbServerStack", cdk_db_vpc = NetworkStack.cdk_db_vpc)

app.synth()
