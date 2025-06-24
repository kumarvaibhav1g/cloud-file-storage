# Cloud File Storage Web App

This is a simple web application built with **Flask** and **Python** that allows users to upload, list, download, and delete files from an **AWS S3** bucket. 
It is designed as a beginner-friendly project to demonstrate how to interact with cloud storage using the AWS SDK (`boto3`).

## Features

- Upload files directly from the browser to an AWS S3 bucket
- List all files currently stored in the bucket
- Download and delete files from the bucket
- Secure handling of AWS credentials and configuration using environment variables (`.env` file)
- Lightweight and easy to extend for cloud computing beginners

## Technologies Used

- Python 3
- Flask web framework
- AWS S3 for cloud storage
- `boto3` AWS SDK for Python
- Environment variables management with `python-dotenv`

## Getting Started

1. Clone the repository
2. Create and activate a Python virtual environment
3. Install dependencies from `requirements.txt`
4. Configure your AWS credentials and S3 bucket info in a `.env` file
5. Run the Flask app locally and start uploading files!
