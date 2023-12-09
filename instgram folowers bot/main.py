from random import randint

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrome_driver_path = "C:\\Users\\Osama Raed Alnobani\\OneDrive\\Desktop\\development\\chromedriver_win32\\chromedriver.exe"


class InstaFollower:

    def __init__(self, username, password,numFollow):
        service = Service(executable_path=chrome_driver_path)
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=option)
        self.username = username
        self.password = password
        self.numFollow = numFollow

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        sleep(5)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(self.username)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

        sleep(5)

    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps/followers/')
        sleep(10)
        # modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     sleep(2)

        for i in range(1, self.numFollow):
            buttons = self.driver.find_element(By.XPATH,
                                               f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button')
            try:
                buttons.click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel.click()


            sleep(randint(1, 4))

    def follow(self):
        pass


bot = InstaFollower("++++++++++++", "000000",20)

bot.login()
bot.find_followers()
bot.follow()
