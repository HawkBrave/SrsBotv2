from selenium import webdriver
from imaplib import IMAP4_SSL
from time import sleep
from datetime import datetime, timezone
import email
import re


class Bot:

    def __init__(self, srs_info, mail_info):
        self.srsuser, self.srspass = srs_info
        self.mailuser, self.mailpass = mail_info
        self.driver = webdriver.Chrome()
        self.mail_service = ''.join(re.search(r"(?:.*@)([\w\.]*)", self.mailuser).groups(1))


    def run(self):
        print("getting to the page..")
        try:
            self.driver.get("https://stars.bilkent.edu.tr")
            self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div/ul/li[3]/a").click()
            self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[1]/div/div/input")\
                    .send_keys(self.srsuser + "\t" + self.srspass + "\n")

        except Exception as e:
            self.driver.close()
            print("oops")
            raise e

        sleep(2)
        print("waiting for the mail server..")

        if self.mail_service == "gmail.com":
            self.mail_service = "imap." + self.mail_service
        elif self.mail_service == "ug.bilkent.edu.tr":
            raise Exception("Please use your gmail account. Bilkent mail is not supported")
        else:
            raise Exception("Invalid email address")

        with IMAP4_SSL(self.mail_service) as m:
            m.login(self.mailuser, self.mailpass)

            m.select("Inbox")
            inbox_item_list = m.search(None, '(FROM "starsmsg@bilkent.edu.tr")')[1][0].split()

            sleep(2)
            print("fetching code from given email address..")
            newest = inbox_item_list[-1]
            raw_mail = m.fetch(newest, '(BODY[TEXT])')[1][0][1].decode('utf-8')

        message = email.message_from_string(raw_mail)
        code = re.search(r" \d{5}", str(message)).group(0).strip()

        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[1]/div/div/input")\
                .send_keys(code + "\n")

        sleep(2)
        print("getting session info from cookies..")
        # print(self.driver.get_cookies())
        expiry = self.driver.get_cookie('PHPSESSID')['expiry']
        session_len = datetime.fromtimestamp(expiry, timezone.utc) - datetime.now(timezone.utc)

        print("waiting for the session to die..")
        sleep(int(session_len.total_seconds()))

        print("session died.. reloging in..")
        self.run()
