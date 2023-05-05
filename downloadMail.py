import imaplib
import email
import os

def downloadPDFs(mail,searchText):
    # search for specific emails by subject or sender
    key = f'(FROM "{mail}" SUBJECT "{searchText}")'
    status,messages = imap.search(None, key)

    mail_id_list = messages[0].split()
    msgs = []

    for num in mail_id_list:
        data = imap.fetch(num, '(RFC822)')
        msgs.append(data)
    
    for response_part_search in msgs[-1]:
            if type(response_part_search) is list:
                for response_part in response_part_search:
                    if type(response_part) is tuple:
                        my_msg=email.message_from_bytes((response_part[1]))
                        print("___________________________")
                        print("Status: ",status)
                        subject = my_msg['subject']
                        print("subj:", subject)
                        print("from:", my_msg['from'])
                        print("body:")
                        for part in my_msg.walk():
                            if part.get_content_type() == 'application/pdf':
                                filename = part.get_filename()
                                if filename:
                                    # create a directory to store the downloaded files
                                    if not os.path.isdir("Download_Mail"):
                                        os.makedirs("Download_Mail")
                                    # download the attachment
                                    filepath = os.path.join("Download_Mail", filename)
                                    with open(filepath, "wb") as f:
                                        f.write(part.get_payload(decode=True))
                                        print(f"Downloaded attachment: {filename}")

user = 'sender_user@gmail.com' # user that send the email
password = '' #this passwords it is from Google appPassword
# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")

try:
    # authenticate
    imap.login(user,password)
except:
    print('Wrong Credentials')

# select mailbox
# if you have multiple mailboxes, you can use imap.list() to view all mailbox
# names and select a specific one using the imap.select() method
imap.select("inbox")
mail = "pdf_from_company@gmail.com" # Email from where you want to download the pdf files
searchText = "Subject to help the search"
downloadPDFs(mail,searchText)

# close the mailbox and logout
imap.close()
imap.logout()