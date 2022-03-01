import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name = 'cpl-backend-bucket'

response = client.delete_bucket(
    Bucket='bucket_name',
)