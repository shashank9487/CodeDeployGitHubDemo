#!/bin/bash
echo "Lambda files got changed. Going to update lambda function code"
aws ssm get-parameters-by-path --path /sctdms --region us-east-1 | jq -r '.Parameters | map(.Name+"="+.Value)| join("\n") | sub("/sctdms/"; ""; "g")  ' >.envmkdir -p /tmp/lamda/Test
echo Copying Files from Project to Temp Folder
rsync -a  Test/ /tmp/lamda/Test/
mv /tmp/lamda/Test/Test.py /tmp/lamda/Test/lambda_function.py
cp .env /tmp/lamda/Test/.env
cd /tmp/lamda/Test/ && zip -rq ../Test.zip .
aws s3 cp /tmp/lamda/Test.zip s3://sctdms/lambda_functions/Test-Lambda/Test.zip
aws lambda update-function-code --function-name getLamData --s3-bucket sctdms --s3-key lambda_functions/Test-Lambda/Test.zip
