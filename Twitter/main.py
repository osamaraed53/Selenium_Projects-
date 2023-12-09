import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Users\\Osama Raed Alnobani\\OneDrive\\Desktop\\development\\chromedriver_win32\\chromedriver.exe"

PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:

    def __init__(self, email, password, username):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=option)
        self.up = 0
        self.down = 0
        self.id = 0
        self.email = email
        self.password = password
        self.username = username

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")

        time.sleep(5)
        self.go_button = self.driver.find_element(By.XPATH,
                                                  '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go_button.click()

        try:
            time.sleep(2)
            self.skip = self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
            self.skip.click()
        except:
            pass

        time.sleep(60)
        result_id = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').text
        self.id = result_id
        download = self.driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = download
        upload = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = upload


    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/")

        time.sleep(2)
        login = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div')
        login.click()
        time.sleep(5)
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(self.email)

        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        try:
            time.sleep(2)
            password = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(self.password)
            password.send_keys(Keys.ENTER)

        except:

            time.sleep(2)
            username = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys(self.username)
            next_button = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
            next_button.click()

            time.sleep(2)
            password = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(self.password)
            password.send_keys(Keys.ENTER)

        # self.login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        # self.login.click()

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 "//div[@data-testid='tweetTextarea_0']")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up? this is test id : {self.id}"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        tweet_button.click()




bot = InternetSpeedTwitterBot("osamaraed53.study@gmail.com", "***************", "*************8")
bot.get_internet_speed()
bot.tweet_at_provider()
