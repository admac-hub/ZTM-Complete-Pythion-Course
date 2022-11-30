import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
 

# email = EmailMessage()
# email['from'] = 'Ardit Cuko'
# email['to'] = 'driticuko8@gmail.com'
# email['subject'] = 'you won 1,000,000 dollars!'

# email.set_content('i am a python master')

email_address = 'engacuko@gmail.com'
email_password = 'remktadlgqmjbvvj'
html = Template(Path('Scripting\\email\\index.html').read_text()) 
email = EmailMessage()
email['from'] = 'Ardit'
email['to'] = 'driticuko8@gmail.com'
email['subject'] = 'You won 1,000,000 dollars !!!'
# building the server connection

with smtplib.SMTP_SSL('smtp.gmail.com') as connection:  
     connection.ehlo()
     connection.starttls()
     connection.login(email_address, email_password )
     connection.send_message(email.set_content(html))
     print('email - sent')




import smtplib 
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
    email_address = 'your_email_sender@gmail.com'
    email_password = 'App_Passwords_is_generated'
    connection.login(email_address, email_password )
    connection.sendmail(from_addr=email_address, to_addrs='receiver_email@something.com', 
    msg= html.substitute(name= 'toto'))