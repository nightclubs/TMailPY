import requests, random



class Mail:
    def __init__(self):
        self.discord = 'blog#8751'
        self.github = 'accusable'
 
    def create_email():
        email = '{}@lasagna.email'.format("".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=10))) # formats random choices into the {}.
        return email

    def get_mail(email):
        with requests.Session() as session:
          base_mail = session.get(
            'https://lasagna.email/api/inbox/{}'.format(email)
          )
          
          if base_mail.json()['emails'] == []:
           return 'No Emails Have Beent Sent!' 

          else: 
            
           return base_mail.json()['emails'] # gets the email response from base_mail json, then returns it for the user.
    
    def check_mail(email_id):
        with requests.Session() as session:
          base_mail = session.get(
            'https://lasagna.email/inbox/email/{}'.format(email_id)
          )
          return base_mail.text # returns the data in a text format so its easy for the user to split it.
  
class Email:
    def __init__(self):
        self.discord = 'blog#8751'
        self.github = 'accusable'
 
    def create_email(domain):
        email = '{}@{}'.format("".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=10)), domain) 
        return email

    def get_mail(email):
        with requests.Session() as session:
          base_mail = session.get(
            'https://lasagna.pro/api/inbox/{}'.format(email)
          )
          
          if base_mail.json()['emails'] == []:
           return 'No Emails Have Beent Sent!' 

          else: 
            
           return base_mail.json()['emails'] 
    
    def check_mail(email_id):
        with requests.Session() as session:
          base_mail = session.get(
            'https://lasagna.pro/inbox/email/{}'.format(email_id)
          )
          return base_mail.text
