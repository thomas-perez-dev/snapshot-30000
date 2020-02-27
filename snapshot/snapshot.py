#import sys
import boto3
import click

session = boto3.Session(profile_name='snapshot')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []

    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances

# @ is a decorator
# Decorator expressions are evaluated when the function is defined
@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project', default=None,
    help="Only instances for project (tag Project:<name>)")
def list_instances(project):
    "List EC2 instances"
   
    instances = filter_instances(project)
    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
            )))
    return

@instances.command('stop')
@click.option('--project', default=None,
    help="Only instances for project (tag Project:<name>)")
def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instances(project)
        
    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
    
    return

@instances.command('start')
@click.option('--project', default=None,
    help="Only instances for project (tag Project:<name>)")
def start_instances(project):
    "Start EC2 instances"

    instances = filter_instances(project)
        
    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()
    
    return

if __name__ == '__main__':
 # Create a list with each comment arguments in it
 # command line: pipenv run python snapshot/snapshot.py instances stop --project=valkyrie
 # result: ['snapshot/snapshot.py', 'instances', 'stop', '--project=valkyrie']
 # we use click, more practical
 #  print(sys.argv)
    
    instances()