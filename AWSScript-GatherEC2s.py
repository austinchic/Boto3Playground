import boto3
import pandas as pd
from botocore.exceptions import ClientError

# Read in access keys from file
# with open("corinnej_accessKeys.csv") as f:
#     for line in f:
#         fields = line.split(',')
#         assert len(fields == 2)
#         (key, value) = fields

# Try Pandas module
data = pd.read_csv('corinnej_accessKeys.csv', skiprows = 1, names=['KeyID', 'AccessKey'])
key_value_pair = data.to_dict(orient='records')

# for pair in key_value_pair:
#     print(data)

first_pair = key_value_pair[0]
keyID = first_pair['KeyID']
accessKey = first_pair['AccessKey']


# Create a boto3 session
session = boto3.Session(
    aws_access_key_id=keyID,
    aws_secret_access_key=accessKey,
    region_name='us-east-1'  # e.g., 'us-east-1'
)

# Create an EC2 client
ec2_client = session.client('ec2')

# Retrieve and print information about EC2 instances
def list_ec2_instances():
    try:
        response = ec2_client.describe_instances()
        instances = response['Reservations']
        if not instances:
            print("No EC2 instances found.")
        else:
            for reservation in instances:
                for instance in reservation['Instances']:
                    print(f"Instance ID: {instance['InstanceId']}")
                    print(f"Instance Type: {instance['InstanceType']}")
                    print(f"Launch Time: {instance['LaunchTime']}")
                    print(f"State: {instance['State']['Name']}")
                    print("Tags: ", instance.get('Tags', 'No Tags'))
                    print("-" * 60)
    except Exception as e:
        print(f"Error retrieving EC2 instances: {e}")

if __name__ == '__main__':
    list_ec2_instances()
