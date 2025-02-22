## S3 Static Website Deployment Tool
This project provides a GUI-based tool to upload a ZIP file containing a static website, extract its contents, and deploy it to an Amazon S3 bucket with a unique deployment link.

## Features
  1 - Upload a ZIP file containing HTML, CSS, JS files
  2 - Extract files and delete previous deployments
  3 - Upload extracted files to an S3 bucket4 - Configure S3 for static website hosting
  4 - Apply public access policies automatically
  5 - Generate a shareable deployment link

## How to use?
  1- Run python gui.py
  2- Click "Upload ZIP File"
  3- Select a ZIP file containing your website
  4- The tool will extract, upload, and generate a deployment URL
  5- Copy the deployment link and share it 
  
## Deployment Process
  1 - The ZIP file is extracted into the website_files/ folder
  2 - Old files are deleted before extracting new ones
  3 - Files are uploaded to an S3 bucket under a unique deployment path
  4 - The S3 bucket policy is updated to allow public access
  5 - A static website hosting configuration is applied
  6 - A unique URL is generated and displayed
