from twilio.rest import Client 
 
account_sid = 'AC1f621ca83b81d0343c1f46cf2ae98d25' 
auth_token = 'bf9a71392d295223bfccec153a7d12d3' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              from_ = '+16402237160', 
                              body='I cant belice this',      
                              to='+12159342512' 
                          ) 
 
print(message.sid)