#!/bin/bash 

build_path=lambda/build/

rm -rf builds/$1.zip

mkdir -p builds
mkdir -p ${build_path}
cp -r common/ ${build_path}
cp -r $1/* ${build_path}
cd ${build_path}
pip install -r requirements.txt -t .

zip -r ../../builds/$1.zip ./*
cd ../../
rm -rf lambda
