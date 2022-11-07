import getopt, sys
import smtplib
 
#Email Variables
#SMTP_SERVER = 'ssl0.ovh.net' #Email Server (don't change!)
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 465 #Server Port (don't change!)
#MAIL_USERNAME = 'notifiche@cbe-elettronica.it' #change this to match your gmail account
MAIL_USERNAME = 'linuxoffice123@gmail.com' #change this to match your gmail account
#MAIL_PASSWORD = 'Email_Notifi45'  #change this to match your gmail password
MAIL_PASSWORD = '123linuxoffice'  #change this to match your gmail password
 
debug = 1

class Emailer:
    def sendmail(self, recipient, subject, content):
         
        #Create Headers
        headers = ["From: " + MAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
 
        if debug: 
            print("Starting")
        #Connect Server
        session = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

        if debug: 
            print("Server Started...")
 
        #Login
        session.login(MAIL_USERNAME, MAIL_PASSWORD)
        if debug: 
            print("Server Login Successful")
        #Send Email & Exit
        session.sendmail(MAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        if debug: 
            print("Sending Message...")
        session.quit
        if debug: 
            print("Quit Server")
 
#sender = Emailer()

#sendTo = 'mauro@cbe-elettronica.it'
#emailSubject = 'Test invio'
#emailContent = 'Test body'

#sender.sendmail(sendTo, emailSubject, emailContent)

def usage():
    print("Error. Usage: python emailer.py -d name@email.com -s mySubject -b myBody")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:s:b:", ["help", "dest=", "subject=", "body="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    dest = None
    subject = ""
    body = ""
    for o, a in opts:
        if o in ("-d", "--dest"):
            dest = a
        elif o in ("-s", "--subject"):
            subject = a
        elif o in ("-b", "--body"):
            body = a
        else:
            assert False, "Opzione non gestita"
    if dest != None:
        if '@' in dest:
            sender = Emailer()
            sender.sendmail(dest, subject, body)
            # print(dest, subject, body)
        else:
            usage()
            sys.exit(2)
    else:
        usage()
        sys.exit(2)


# if __name__ == "__main__":
#     main()
