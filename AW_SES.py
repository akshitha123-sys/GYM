import boto3

# Creating an SES client
client = boto3.client('ses')

# Verifying email addresses for sending email
response = client.verify_email_identity(
    EmailAddress='admin@example.com'
)
print(response)

response = client.verify_email_identity(
    EmailAddress='user@example.com'
)
print(response)

# Creating a new email template
response = client.create_template(
    Template={
        'TemplateName': 'GymManagementNotification',
        'SubjectPart': 'Gym Management Notification',
        'TextPart': 'Hi,\n\nThis is to notify you about your gym membership status.\n\nThanks,\nThe Gym Management Team',
        'HtmlPart': '<html><body><p>Hi,</p><p>This is to notify you about your gym membership status.</p><p>Thanks,</p><p>The Gym Management Team</p></body></html>'
    }
)
print(response)
