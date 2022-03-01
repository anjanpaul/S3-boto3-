import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name = 'cpl-backend-bucket'
file_upload= s3.Bucket('bucket_name').upload_file('README.md', 'README.md')

print(file_upload)
