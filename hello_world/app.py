import json
import boto3


def lambda_handler(event, context):
    pipeline = boto3.client('codepipeline')
    print('event', event)
    print('context', context)
    jobId=event['CodePipeline.job']['id']
    response = pipeline.put_job_success_result(
        jobId=jobId
    )
    return response
