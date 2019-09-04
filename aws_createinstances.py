import boto3
ec2_resource = boto3.resource('ec2')
ec2 = boto3.client('ec2')
list_ec2 = ec2_resource.create_instances(ImageId='ami-07d0cf3af28718ef8', KeyName='naveen_techie', InstanceType='t2.micro', MinCount=1, MaxCount=2)
ec2_created = [ec2_instance.id for ec2_instance in list_ec2]
print(ec2_created)
