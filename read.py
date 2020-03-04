# Author

import imaplib
import base64
import os
import email

email_user = '@gmail.com'
email_pass = 'pwd'

imap_url = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imap_url) 

con.login(email_user, email_pass)

con.select('Inbox')

type, data = con.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = con.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
    
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1].decode('utf-8'))
            email_subject = msg['subject']
            email_from = msg['from']
            print ('From : ' + email_from + '\n')
            print ('Subject : ' + email_subject + '\n')
            print(msg.get_payload(decode=True))
