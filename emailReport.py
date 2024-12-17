# emailReport.py
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def send_sns_email():
    # Initialize a boto3 SNS client
    sns_client = boto3.client('sns', region_name='us-east-1')  # Specify your region here
    
    # Replace with your SNS topic ARN
    topic_arn = 'arn:aws:sns:us-east-1:123456789012:simpleRobotTestTopic'
    
    # Message content
    message = "This is an email sent via SNS from Robot Framework test case."
    subject = "SNS Email Notification"
    
    try:
        # Publish message to the SNS topic
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject
        )
        
        print(f"Message sent! Message ID: {response['MessageId']}")
        
    except (NoCredentialsError, PartialCredentialsError):
        print("Error: AWS credentials are not configured properly.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_sns_email()
