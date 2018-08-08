# AWS Lambda URL Shortener

This is a POC for a url shortening service using AWS APIGW, Lambda and DynamoDB

## Endpoints

### Create short url
`curl -X POST http://YOUR_ID.execute-api.eu-west-1.amazonaws.com/Prod/ --data "{ \"url\":\"https://github.com\"}"`

### Expand short url
`curl -X GET http://YOUR_ID.execute-api.eu-west-1.amazonaws.com/Prod/{linkId}"`

## How to deploy to AWS
1. Install aws-sam-cli `pip install aws-sam-cli`
2. Build the lambdas `./build_lambda.sh get_short_url`
3. Build the lambdas `./build_lambda.sh create_short_url`
4. Package the template `sam package --template-file template.yaml --s3-bucket YOUR_CFT_BUCKET --output-template-file packaged.yaml`
    YOUR_CFT_BUCKET can be a new empty bucket.
5. Deploy `aws cloudformation deploy --template-file /path/to/file/packaged.yaml --stack-name Url-Shortener-Stack --capabilities CAPABILITY_IAM`
6. Navigate to the AWS Console -> Api Gateway -> Your New Api (Url-Shortener)-> Root resource (/) -> Actions -> Deploy Api
7. Voila!

## How to run this localy 
1. Install aws-sam-cli `pip install aws-sam-cli`
2. Install docker
3. Build the lambda `./build_lambda.sh get_short_url`
4. Run sam `sam local start-api`

You should have a new container running and listening on http://127.0.0.1:3000



This is an early stage WIP/MVP. 