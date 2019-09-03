# This script will retrive the active AWS ec2 instance details and shows the status as list
####################

import boto3
import pprint as pprint
import pandas as pd
ec2 = boto3.client('ec2')

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


response = ec2.describe_instances()
ec2_list = ec2status(response)
print(ec2_list)
