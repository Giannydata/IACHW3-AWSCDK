import aws_cdk as core
import aws_cdk.assertions as assertions

from hw3_cdk_db_server.hw3_cdk_db_server_stack import Hw3CdkDbServerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in hw3_cdk_db_server/hw3_cdk_db_server_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Hw3CdkDbServerStack(app, "hw3-cdk-db-server")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
