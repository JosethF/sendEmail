from email.message import EmailMessage
import ssl
import smtplib
import os

email_sender = 'your_user@gmail.com'
email_password = '' #this passwords it is from Google appPassword
email_receiver = ''

subject = 'sendMail attempt 1'
body = """
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

# Directory containing PDF files
pdf_dir = 'Download_Mail'

# Loop through the directory and attach each PDF file to the email
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        with open(os.path.join(pdf_dir, filename), 'rb') as f:
            file_data = f.read()
            em.add_attachment(file_data, maintype='application', subtype='pdf', filename=filename)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())