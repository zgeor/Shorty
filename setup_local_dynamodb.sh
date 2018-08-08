#!/bin/bash
if [ ! -d dynamodb ]; then
    mkdir dynamodb
    cd dynamodb
    curl -L https://s3.eu-central-1.amazonaws.com/dynamodb-local-frankfurt/dynamodb_local_latest.tar.gz -O 
    tar xzvf dynamodb_local_latest.tar.gz
    cd ../
fi

cd dynamodb
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb