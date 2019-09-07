import boto3
import pprint as pprint
import pandas as pd
from botocore.exceptions import ClientError
ec2_resource = boto3.resource('ec2')
ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
print(vpc_id)
#Variable Declaration
grp_name = "custom_naveen"
ami_id = "ami-07d0cf3af28718ef8"
key_name = "naveen_techie"
inst_type = "t2.micro" 

#Function supposed to create Security Group
def create_sgrp():
    grp_name = 'custom_naveen'
    try:
        ec2_sg = ec2.create_security_group(GroupName=grp_name, Description='Created over boto3', VpcId=vpc_id)
        security_group_id = ec2_sg['GroupId']
        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
        sg_data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol' : 'tcp',
             'FromPort' : 22,
             'ToPort' :22,
             'IpRanges' : [{'CidrIp': '0.0.0.0/0', 'Description': "Created over boto3" }]},
            {'IpProtocol' : 'tcp',
             'FromPort' : 80,
             'ToPort' : 80,
             'IpRanges' : [{'CidrIp': '0.0.0.0/0', 'Description': "Created over boto3"}]}
        ])
        print('Ingress created Succesfully %s.' % sg_data)
    except ClientError as e:
        print(e)

#Instance Creation        
def create_instance():
    ec2_resource.create_instances(ImageId=ami_id, KeyName=key_name,SecurityGroups=[grp_name] ,InstanceType=inst_type, MinCount=1, MaxCount=1)

#Generate Status    
def ec2status(response):
    av_zones = []
    inst_ids = []
    state_name = []
    for res in response['Reservations']:
        for ins in res['Instances']:
            av_zones.append(ins['Placement']['AvailabilityZone'])
            inst_ids.append(ins['InstanceId'])
            state_name.append(ins['State']['Name'])
    return pd.DataFrame({'InstanceIds': inst_ids, 'Availability Zone': av_zones, 'State': state_name})

def ec2status(response):
    av_zones = []
    inst_ids = []
    state_name = []
    for res in response['Reservations']:
        for ins in res['Instances']:
            av_zones.append(ins['Placement']['AvailabilityZone'])
            inst_ids.append(ins['InstanceId'])
            state_name.append(ins['State']['Name'])
    return pd.DataFrame({'InstanceIds': inst_ids, 'Availability Zone': av_zones, 'State': state_name})


create_sgrp()
create_instance()
response = ec2.describe_instances()
ec2_list = ec2status(response)
print(ec2_list)
