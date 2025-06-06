from cdk_stack import algoserv_stack
import aws_cdk as cdk

app = cdk.App()
# instantiate the stacks
algoserv_stack.AlgoservStack(app,"AlgoservStack",env=cdk.Environment(account='507803686269', region='us-east-1'))
app.synth()