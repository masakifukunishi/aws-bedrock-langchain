from langchain_community.llms import Bedrock
import boto3

client = boto3.client("bedrock-runtime")
model = Bedrock(client=client, model_id="anthropic.claude-instant-v1")

print(model("Hello, Who are you?"))