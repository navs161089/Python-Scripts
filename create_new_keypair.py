import boto3
ec2 = boto3.resource('ec2')
key_name = 'naveen_test'
new_keypair = ec2.create_key_pair(KeyName=key_name)
with open('/home/key/naveen_test.pem', 'w') as file:
    file.write(new_keypair.key_material)
    print(new_keypair.key_fingerprint)
