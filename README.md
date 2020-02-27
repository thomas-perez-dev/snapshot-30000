# snapshotalyzer-30000

Demo project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage EC2 instance snapshots.

## Configuring

snapshot uses the configuration file created by the AWS CLI

`aws configure --profile snapshot`

## Running

`pipenv run python snapshot/snapshot.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional
