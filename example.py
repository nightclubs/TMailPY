from wrapper import *

mail = Mail # no args are given so you dont have to do Mail(), if you do Mail() it will mess with the code.

def get_email():
 print('generated email >> {}'.format(mail.create_email()))

# get_email()

def get_emails():
 print('mail >> {}'.format(mail.get_mail('test@lasagna.email')))

# get_emails()

def check_mail():
 print('content >> {}'.format(mail.check_mail('mail id'))) # the mail ID is the numbers in the link, you will see mail id when you use the get_emails function.

# check_mail()
