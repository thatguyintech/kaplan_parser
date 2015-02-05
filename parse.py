import imaplib
import datetime
import re

def mailstuff(mail_conf):
    # prepare output file
    output_file = open(mail_conf["output"], "w")

    # login and open inbox
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(mail_conf["login"], mail_conf["password"])
    mail.select("inbox")
    date = (datetime.date.today() - datetime.timedelta(mail_conf["lookback"])).strftime("%d-%b-%Y")

    # look for relevant mail
    result, data = mail.search(None, '(SENTSINCE {date} HEADER Subject "{subject}")'.format(date=date, subject=mail_conf["criteria"]))

    # data is a list of e-mail ids
    ids = data[0] 
    id_list = ids.split()

    for id_num in id_list: 
        message = mail.fetch(id_num, "(RFC822)")[1][0][1]
        decoded_message = message.decode('UTF-8', 'ignore')
        match = re.search("Name:\s*(?P<name>[\w ]*)", decoded_message)
        output_file.write(match.group("name")+"\n")

    output_file.close()

def main():
    mail_conf = {}
    mail_conf["login"] = input("Login email: ") # gmail
    mail_conf["password"] = input("Password: ") # derp
    mail_conf["lookback"] = input("Number of days to search through: ") # 2
    mail_conf["criteria"] = input("Subject line search: ") # Theta Tau - Kaplan
    mail_conf["output"] = input("File to write to: ") # names.txt

    mailstuff(mail_conf)

if __name__ == "__main__":
    main()
