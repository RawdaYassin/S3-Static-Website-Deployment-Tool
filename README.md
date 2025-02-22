## S3 Static Website Deployment Tool
This project provides a GUI-based tool to upload a ZIP file containing a static website, extract its contents, and deploy it to an Amazon S3 bucket with a unique deployment link.

## Features
  - Upload a ZIP file containing HTML, CSS, JS files
  - Extract files and delete previous deployments
  - Upload extracted files to an S3 bucket4 - Configure S3 for static website hosting
  - Apply public access policies automatically
  - Generate a shareable deployment link

## How to use?
  - Run python gui.py
  - Click "Upload ZIP File"
  - Select a ZIP file containing your website
  - The tool will extract, upload, and generate a deployment URL
  - Copy the deployment link and share it 
  
## Deployment Process
  - The ZIP file is extracted into the website_files/ folder
  - Old files are deleted before extracting new ones
  - Files are uploaded to an S3 bucket under a unique deployment path
  - The S3 bucket policy is updated to allow public access
  - A static website hosting configuration is applied
  - A unique URL is generated and displayed
