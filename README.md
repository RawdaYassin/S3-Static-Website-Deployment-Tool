S3 Static Website Deployment Tool 
This project provides a GUI-based tool to upload a ZIP file containing a static website, extract its contents, and deploy it to an Amazon S3 bucket with a unique deployment link.

📌 Features
✅ Upload a ZIP file containing HTML, CSS, JS files
✅ Extract files and delete previous deployments
✅ Upload extracted files to an S3 bucket
✅ Configure S3 for static website hosting
✅ Apply public access policies automatically
✅ Generate a shareable deployment link

🛠 Setup Instructions
1️⃣ Install Required Dependencies
Ensure you have Python installed, then install the required libraries:

sh
Copy
Edit
pip install boto3 tkinter
2️⃣ Configure AWS Credentials
Set up your AWS access keys as environment variables:



sh
Copy
Edit
aws configure
3️⃣ Set Up S3 Bucket
Enable Static Website Hosting for your S3 bucket
Make sure your bucket name and region match in s3_manager.py
🖥️ How to Use
Option 1: Run the GUI
Run the GUI to select and upload a ZIP file:

sh
Copy
Edit
python gui.py
Click "Upload ZIP File"
Select a ZIP file containing your website
The tool will extract, upload, and generate a deployment URL
Copy the deployment link and share it 🎉
📂 Project Structure
graphql
Copy
Edit
📁 project_root/
│-- gui.py            # GUI for uploading ZIP files
│-- s3_manager.py     # Handles S3 file uploads & deployment
│-- website_files/    # Extracted files from the ZIP
│-- README.md         # Project documentation
🌍 Deployment Process
1️⃣ The ZIP file is extracted into the website_files/ folder
2️⃣ Old files are deleted before extracting new ones
3️⃣ Files are uploaded to an S3 bucket under a unique deployment path
4️⃣ The S3 bucket policy is updated to allow public access
5️⃣ A static website hosting configuration is applied
6️⃣ A unique URL is generated and displayed

🔗 Example Deployment Link
After a successful deployment, your website will be accessible at:

bash
Copy
Edit
http://ghaymah-course-bucket.s3-website-us-east-2.amazonaws.com/rawda/{deployment_id}/index.html
Replace {deployment_id} with your actual deployment identifier.

🚀 Next Steps
Add a copy button to easily copy the deployment link
Enhance the GUI with progress indicators
Implement an automatic domain setup using CloudFront
Happy Deploying! 🎉🚀