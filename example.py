from wrapper import *

mail = Mail

def get_email():
 print('generated email >> {}'.format(mail.create_email()))

# get_email()

def get_emails():
 print('mail >> {}'.format(mail.get_mail('test@lasagna.email')))

# get_emails()

def check_mail():
 print('content >> {}'.format(mail.check_mail('mail id'))) # the mail ID is the numbers in the link, you will see mail id when you use the get_emails function.

# check_mail()
