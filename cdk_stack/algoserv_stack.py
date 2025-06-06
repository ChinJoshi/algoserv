from aws_cdk import Stack, aws_lambda as lambda_, CfnOutput
from constructs import Construct


class AlgoservStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope,construct_id,**kwargs)
        serverless_function = lambda_.Function(scope=self,
                                               id="Algoserv app function",
                                               code=lambda_.Code.from_asset("lambda"),
                                               handler="app.main.handler",
                                               runtime=lambda_.Runtime.PYTHON_3_13)
        function_url = serverless_function.add_function_url(auth_type=lambda_.FunctionUrlAuthType.NONE)
        CfnOutput(scope=self,id="Algoserv app function url",value=function_url.url)