import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import logging
from datetime import datetime

# Set logging configuration
logging.basicConfig(filename='backup_report.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
SOURCE_DIR = '/path/to/source_directory'  # Directory to backup
BUCKET_NAME = 'your-bucket-name'  # S3 bucket name
REMOTE_DIR = 'backup/'  # Remote directory in the bucket
AWS_REGION = 'your-region'  # AWS region (e.g., 'us-east-1')

def upload_to_s3(file_path, bucket_name, remote_dir):
    """Uploads a file to S3 bucket."""
    s3 = boto3.client('s3', region_name=AWS_REGION)
    try:
        file_name = os.path.basename(file_path)
        s3.upload_file(file_path, bucket_name, os.path.join(remote_dir, file_name))
        logging.info(f"Successfully uploaded {file_path} to {bucket_name}/{remote_dir}")
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
    except NoCredentialsError:
        logging.error("Credentials not available.")
    except PartialCredentialsError:
        logging.error("Incomplete credentials provided.")
    except Exception as e:
        logging.error(f"Failed to upload {file_path}: {e}")

def backup_directory(source_dir, bucket_name, remote_dir):
    """Backups up the specified directory to S3."""
    if not os.path.isdir(source_dir):
        logging.error(f"Source directory {source_dir} does not exist.")
        return

    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            upload_to_s3(file_path, bucket_name, remote_dir)

def main():
    """Main function to run the backup."""
    logging.info("Backup operation started.")
    start_time = datetime.now()

    backup_directory(SOURCE_DIR, BUCKET_NAME, REMOTE_DIR)

    end_time = datetime.now()
    duration = end_time - start_time
    logging.info(f"Backup operation completed. Duration: {duration}")

if __name__ == "__main__":
    main()
