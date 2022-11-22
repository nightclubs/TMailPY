from wrapper import *

mail = TMailPY

def new_email():
    email = mail.create_email()
    return email

def get_mail():
    emails = mail.get_mail(new_email())
    return emails

def check_mail():
    email_ids = mail.check_mail(get_mail())
    return email_ids





