from selenium import webdriver
from time import sleep

class Bot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()


    def run(self):
        print("starting")

        self.driver.get("https://stars.bilkent.edu.tr")
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div/ul/li[3]/a").click()
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/section/form/fieldset/div/div[1]/div[1]/div/div/input")\
                .send_keys(self.username + "\t" + self.password + "\n")

        sleep(2)
