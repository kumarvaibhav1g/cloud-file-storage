from flask import Flask, render_template, request, redirect, send_file
import boto3
import os
from dotenv import load_dotenv
from botocore.config import Config
import tempfile

# Load environment variables
load_dotenv()

app = Flask(__name__)

S3_BUCKET = os.getenv("S3_BUCKET")
S3_REGION = os.getenv("S3_REGION")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

s3 = boto3.client('s3',
    region_name=S3_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

s3 = boto3.client(
    's3',
    region_name=S3_REGION,
    endpoint_url=f'https://s3.{S3_REGION}.amazonaws.com',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

@app.route('/')
def index():
    objects = s3.list_objects_v2(Bucket=S3_BUCKET).get('Contents', [])
    files = [obj['Key'] for obj in objects]
    return render_template('index.html', files=files, bucket=S3_BUCKET, region=S3_REGION)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        s3.upload_fileobj(file, S3_BUCKET, file.filename)
    return redirect('/')

@app.route('/delete/<filename>')
def delete(filename):
    s3.delete_object(Bucket=S3_BUCKET, Key=filename)
    return redirect('/')

@app.route('/download/<filename>')
def download(filename):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        s3.download_fileobj(S3_BUCKET, filename, tmp)
        tmp.seek(0)
        return send_file(tmp.name, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(debug=True)


