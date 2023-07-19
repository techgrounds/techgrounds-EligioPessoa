import aws_cdk as core
import aws_cdk.assertions as assertions

from pro_1_1_cdk.pro_1_1_cdk_stack import Pro11CdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in pro_1_1_cdk/pro_1_1_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Pro11CdkStack(app, "pro-1-1-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
