# AWS Lambda URL Shortener

This is a POC for a url shortening service using AWS APIGW, Lambda and DynamoDB

## Endpoints

### Create short url
TBI

### Expand short url
TBI

## How to deploy this on AWS
TBI

## How to run this localy 
1. Install aws-sam-cli `pip install aws-sam-cli`
2. Install docker
3. Build the lambda `./build_lambda.sh get_short_url`
4. Run sam `sam local start-api`

You should have a new container running and listening on http://127.0.0.1:3000
