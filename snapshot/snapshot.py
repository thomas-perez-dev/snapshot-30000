#import sys
import boto3
import click

session = boto3.Session(profile_name='snapshot')
ec2 = session.resource('ec2')

# @ is a decorator
# Decorator expressions are evaluated when the function is defined
@click.command()
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return

if __name__ == '__main__':
 # Create a list with each comment arguments in it
 # command line: pipenv run python snapshot/snapshot.py instances stop --project=valkyrie
 # result: ['snapshot/snapshot.py', 'instances', 'stop', '--project=valkyrie']
 # we use click, more practical
 #  print(sys.argv)
    
    list_instances()