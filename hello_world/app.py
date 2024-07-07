import json
import boto3


def lambda_handler(event, context):
    pipeline = boto3.client('codepipeline')
    jobId=event['CodePipeline.job']['id']
    url = event["CodePipeline.job"].data.actionConfiguration.configuration.UserParameters; 
    response = pipeline.put_job_success_result(
        jobId=jobId
    )
    return response
