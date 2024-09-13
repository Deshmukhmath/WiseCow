How the script works:
Configuration: Set up the source directory to back up, S3 bucket name, remote directory in the bucket, and AWS region.
Upload Function: upload_to_s3() uploads a single file to the specified S3 bucket.
Backup Function: backup_directory() walks through the source directory and uploads each file to the S3 bucket using the upload_to_s3() function.
Main Function: main() logs the start time, performs the backup, logs the end time, and calculates the duration.
Customization:
Remote Storage: If you're using a different cloud storage provider or remote server, you will need to adjust the upload logic accordingly. For example, you might use paramiko for SFTP backups or an API for another cloud provider.
Error Handling: This script includes basic error handling for file not found, credentials issues, and other exceptions. You can expand this based on your needs.