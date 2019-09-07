import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
print(vpc_id)
try:
    ec2_sg = ec2.create_security_group(GroupName='custom_naveen', Description='Created over boto3', VpcId=vpc_id)
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
