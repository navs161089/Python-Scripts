import boto3
pyec2 = boto3.resource('ec2')
#Create Custom VPC
cust_vpc = pyec2.create_vpc(CidrBlock='10.0.0.0/16')
cust_vpc.create_tags(Tags=[{"Key":"Name","Value":"py_custvpc"}])
cust_vpc.wait_until_available()
cust_vpcid = cust_vpc.id
print("Created the VPC:")
print(cust_vpc.id)

#Create Subnet1
subnet1 = pyec2.create_subnet(VpcId=cust_vpc.id, AvailabilityZone='us-east-1b', CidrBlock='10.0.1.0/24')
#Create Subnet2
subnet2 = pyec2.create_subnet(VpcId=cust_vpc.id, AvailabilityZone='us-east-1f', CidrBlock='10.0.2.0/24')

print("Created two subnets in different AV zones:")
print(subnet1.id)
print(subnet2.id)


#Create Internet GateWay and attach to the VPC
ig_boto3 = pyec2.create_internet_gateway()
cust_vpc.attach_internet_gateway(InternetGatewayId=ig_boto3.id)

print(ig_boto3.id)

#Create Routing table and a public route
rtable_boto3 = cust_vpc.create_route_table()
route_boto3 = rtable_boto3.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig_boto3.id
)
print(rtable_boto3.id)

#Associate Route Table with subnet
rtable_boto3.associate_with_subnet(SubnetId=subnet1.id)
rtable_boto3.associate_with_subnet(SubnetId=subnet2.id)
