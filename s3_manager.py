import os
import uuid
import json
import boto3

S3_BUCKET_NAME = "ghaymah-course-bucket"
S3_WEBSITE_REGION = "us-east-2"

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("GHAYMAH_AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("GHAYMAH_AWS_SECRET_KEY"),
    region_name=S3_WEBSITE_REGION
)

def generate_unique_id():
    """ Generate a short unique identifier for each deployment """
    return str(uuid.uuid4())[:8]

def upload_files_to_s3(local_folder, deployment_id):
    """ Uploads extracted website files to S3 under a unique deployment path """
    deployment_path = f"rawda/{deployment_id}/"

    try:
        for root, _, files in os.walk(local_folder):
            for file in files:
                file_path = os.path.join(root, file)
                s3_key = os.path.join(deployment_path, os.path.relpath(file_path, local_folder))
                
                # Upload file to S3 with public read access
                s3.upload_file(file_path, S3_BUCKET_NAME, s3_key)
                print(f"✅ Uploaded: {file_path} → s3://{S3_BUCKET_NAME}/{s3_key}")

        # ✅ Set public access policies after uploading files
        set_bucket_policy(deployment_path)
        disable_public_access_block()

        print(f"🚀 All files uploaded successfully for deployment: {deployment_id}")

    except Exception as e:
        print(f"❌ Error uploading files: {str(e)}")

def configure_static_website():
    """ Enables static website hosting on S3 """
    try:
        website_configuration = {
            "ErrorDocument": {"Key": "error.html"},
            "IndexDocument": {"Suffix": "index.html"}
        }
        s3.put_bucket_website(Bucket=S3_BUCKET_NAME, WebsiteConfiguration=website_configuration)
        print(f"✅ Static website hosting enabled for: {S3_BUCKET_NAME}")
    except Exception as e:
        print(f"❌ Error configuring website: {str(e)}")

def get_deployment_url(deployment_id):
    """ Generates the website URL for the uploaded deployment """
    return f"http://{S3_BUCKET_NAME}.s3-website-{S3_WEBSITE_REGION}.amazonaws.com/rawda/{deployment_id}/index.html"

def set_bucket_policy(folder_name):
    """ Sets a public-read policy for the uploaded folder in the S3 bucket """
    try:
        policy = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Sid': 'PublicReadGetObject',
                    'Effect': 'Allow',
                    'Principal': '*',
                    'Action': ['s3:GetObject'],
                    'Resource': [f'arn:aws:s3:::{S3_BUCKET_NAME}/{folder_name}*'] 
                }
            ]
        }
        s3.put_bucket_policy(Bucket=S3_BUCKET_NAME, Policy=json.dumps(policy))
        print(f"✅ Public access policy applied to: {S3_BUCKET_NAME}/{folder_name}")
    except Exception as e:
        print(f"❌ Error setting bucket policy: {str(e)}")

def disable_public_access_block():
    """ Disables public access blocking to allow public access to files """
    try:
        s3.put_public_access_block(
            Bucket=S3_BUCKET_NAME,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )
        print(f"✅ Public access block disabled for bucket: {S3_BUCKET_NAME}")
    except Exception as e:
        print(f"❌ Error disabling public access block: {str(e)}")
