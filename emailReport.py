import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import xml.etree.ElementTree as ET

# Function to generate the test report from the XML file
def generate_test_report(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialize counters for pass, fail, and total tests
    pass_count = 0
    fail_count = 0
    total_count = 0

    # Iterate through the test results in the XML
    for test in root.findall(".//test"):
        status = test.find(".//status").get('status')
        total_count += 1
        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1

    # Calculate pass and fail percentages
    pass_percentage = (pass_count / total_count) * 100 if total_count > 0 else 0
    fail_percentage = (fail_count / total_count) * 100 if total_count > 0 else 0

    # Generate the report
    report = f"Test Results Report\n"
    report += f"---------------------\n"
    report += f"Total Tests: {total_count}\n"
    report += f"Pass: {pass_count} ({pass_percentage:.2f}%)\n"
    report += f"Fail: {fail_count} ({fail_percentage:.2f}%)\n"

    return report

# Function to send the SNS email
def send_sns_email():
    # Initialize a boto3 SNS client
    sns_client = boto3.client('sns', region_name='us-east-2')  # Specify your region here
    
    # Replace with your SNS topic ARN
    topic_arn = 'arn:aws:sns:us-east-2:699475924651:simpleRobotTestTopic'
    
    # Generate the test report
    xml_file = 'output.xml'  # Path to your output.xml file
    message = generate_test_report(xml_file)  # Get the report content
    
    subject = "SNS Email Notification: Test Results"
    
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

# Call the send_sns_email function to send the email
if __name__ == "__main__":
    send_sns_email()
