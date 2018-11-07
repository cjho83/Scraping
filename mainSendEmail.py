# Send email
# https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
#

from string import Template
# import the smtplib module. It should be included in Python by default
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Function to read the contacts from a given contact file and return a
# list of names and email addresses
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


# Function to read an email template from a given message file and return
# a template body
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

<<<<<<< HEAD
def load_login_details():
    with open('login.txt', 'r', encoding='utf-8') as login_file:
        username = login_file.readline()
        password = login_file.readline()
    return username, password


def main():
    #MY_ADDRESS = 'cjho@live.com'
    #PASSWORD = ''
    MY_ADDRESS, PASSWORD = load_login_details()
=======

def main():
    MY_ADDRESS = ''
    PASSWORD = ''
>>>>>>> 6a93f98b36551a601833b715ff2fa05eb3a2e075

    # set up the SMTP server
    names, emails = get_contacts('mycontacts.txt')  # read contacts
    message_template = read_template('message.txt')

<<<<<<< HEAD
    #s = smtplib.SMTP_SSL(host='smtp-mail.outlook.com', port=587)
    #s.starttls()
    #s.login(MY_ADDRESS, PASSWORD)
    s = smtplib.SMTP_SSL('smtp.gmail.com',465)
    s.ehlo()
=======
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
>>>>>>> 6a93f98b36551a601833b715ff2fa05eb3a2e075
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
<<<<<<< HEAD
        # s.send_message(msg)
=======
        s.send_message(msg)
>>>>>>> 6a93f98b36551a601833b715ff2fa05eb3a2e075

        del msg

if __name__ == '__main__':
    main()
