import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')


bucket = s3.create_bucket(
    Bucket='cpl-backend-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-gov-west-1'
    }
)

print(bucket)
    
