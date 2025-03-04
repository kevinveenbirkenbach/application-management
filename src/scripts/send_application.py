import os
import json
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Load environment variables
load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
USERNAME = os.getenv('SMTP_USERNAME')
PASSWORD = os.getenv('SMTP_PASSWORD')

def send_applications():
    # Load the data from the JSON file
    with open('../data/companies.json', 'r+') as f:
        data = json.load(f)

        # Loop through each company
        for company in data['companies']:
            # Loop through each contact
            for contact in company['contacts']:
                # Loop through each position
                for position in contact['positions']:
                    # If the application has not been sent
                    if position['application_status'] != 'sent':
                        # Create the email message
                        msg = MIMEMultipart()
                        msg['From'] = USERNAME
                        msg['To'] = contact['email']
                        msg['Subject'] = f'Application for {position["position_name"]}'

                        # Attach the cover letter and CV
                        for file in [f'../data/{company["name"]}_{position["position_name"]}_cover_letter.pdf',
                                     f'../data/{company["name"]}_{position["position_name"]}_cv.pdf']:
                            attachment = open(file, 'rb')
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload((attachment).read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', 'attachment; filename= ' + os.path.basename(file))
                            msg.attach(part)

                        # Send the email
                        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                        server.login(USERNAME, PASSWORD)
                        server.sendmail(USERNAME, contact['email'], msg.as_string())
                        server.quit()

                        # Update the application status
                        position['application_status'] = 'sent'

        # Save the updated data back to the JSON file
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

if __name__ == "__main__":
    send_applications()