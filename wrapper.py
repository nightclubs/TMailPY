import requests, random


class TMailPY:
    def create_email():
        email = '%s@lasagna.email' % "".join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=10))
        return email

    def get_mail(email):
        with requests.Session() as session:
          base_mail = session.get(
            'https://lasagna.email/api/inbox/%s' % email
          )
          
          if base_mail.json()['emails'] == []:
           return 'No Emails Have Beent Sent!' 

          else: 
            
           return base_mail.json()['emails']
    
    def check_mail(email_id):
        with requests.Session() as session:
          base_mail = session.get(
            'https://lasagna.email/inbox/email/%s' % email_id
          )
          return base_mail.text
