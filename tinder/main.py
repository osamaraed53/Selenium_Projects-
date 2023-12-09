from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Users\\Osama Raed Alnobani\\OneDrive\\Desktop\\development\\chromedriver_win32\\chromedriver.exe"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=option)

driver.get(url="https://tinder.com/")
sleep(3)
try:
    accept = driver.find_element(By.XPATH, '//*[@id="s1862123046"]/div/div[2]/div/div/div[1]/div[1]/button')
    accept.click()
except:
    pass

login = driver.find_element(By.XPATH,
                            '//*[@id="s1862123046"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

sleep(2)
loginByFacebook = driver.find_element(By.XPATH,
                                      '//*[@id="s133741970"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
loginByFacebook.click()

original_window = driver.current_window_handle

window_handle = driver.window_handles[1]
driver.switch_to.window(window_handle)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys("os_ra@mail.ru")

password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys("*************")

login_button = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
login_button.click()

driver.switch_to.window(original_window)

sleep(6)
allow = driver.find_element(By.XPATH, '//*[@id="s133741970"]/main/div/div/div/div[3]/button[1]')
allow.click()

sleep(2)
notInterested = driver.find_element(By.XPATH, '//*[@id="s133741970"]/main/div/div/div/div[3]/button[2]')
notInterested.click()

sleep(6)

for i in range(0, 100):
    try:
        sleep(2)
        p = driver.find_element(By.XPATH,
                                '//*[@id="s1862123046"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span')
        p.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

