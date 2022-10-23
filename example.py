from wrapper import *

mail = Mail

def get_email():
 print('generated email >> {}'.format(mail.create_email()))


def get_emails():
 print('mail >> {}'.format(mail.get_mail('test@lasagna.email')))


def check_mail():
 print('content >> {}'.format(mail.check_mail('mail id'))) # the mail ID is the numbers in the link, you will see mail id when you use the get_emails function.


# ----------------------------------- This top part uses lasagna.email domain only, the bottom part has 2 - 3 different domains!


email = Email

def get_email():
 print('generated email >> {}'.format(email.create_email('domain here'))) # the domains are @lasagna.pro, @rblx.rocks and @linustechtips.email


def get_emails():
 print('mail >> {}'.format(email.get_mail('test@lasagna.pro'))) # you could also choose from the other domains listed above!


def check_mail():
 print('content >> {}'.format(email.check_mail('mail id')))


