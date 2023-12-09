# try:
#     sleep(5)
#     jobs = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div/li-icon/svg/path')
#     jobs.click()
# except Exception:
#     sleep(5)
#     jobs = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div')
#     jobs.click()

# sleep(2)
# search = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember22"]')
# search.clear()
# search.send_keys("internship")
# location = driver.find_element(By.XPATH,'//*[@id="jobs-search-box-location-id-ember22"]')
# search.clear()
# location.send_keys("Jordan")
# location.send_keys(Keys.ENTER)

# sleep(5)
# easy_apply = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
# easy_apply.click()
from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver = "C:\\Users\\Osama Raed Alnobani\\OneDrive\\Desktop\\development\\chromedriver_win32\\chromedriver.exe"

service = Service(executable_path=chrome_driver)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.get(url="https://www.linkedin.com/")

login = driver.find_element(By.ID, "session_key").send_keys("osamaraed53@gmail.com")
password = driver.find_element(By.ID, "session_password").send_keys("*****************")
signin = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button').click()

driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3537589284&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

all_listings = driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list-container li')

for listing in all_listings:
    id_n = listing.get_attribute("id")
    if id_n != "":
        print("id_n",id_n)
    else:
        continue
    print("called")
    listing.click()
    sleep(2)

    try:
        query1 = driver.find_element(By.ID,id_n)
        query1.click()
        sleep(5)
        query2= driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
        query2.click()
        sleep(5)
        query3 = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]')
        query3.click()
        sleep(4)
        query4 = driver.find_element(By.XPATH,'//*[@id="ember395"]/div[2]/div[2]/div[2]/div[1]/div[1]/button')
        query4.click()
        driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3537589284&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
        sleep(5)

    except NoSuchElementException:
        print("No application button, skipped.")
        driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3537589284&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
        sleep(5)
        continue
