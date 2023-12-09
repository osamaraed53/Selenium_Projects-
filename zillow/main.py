from pprint import pprint
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61529005957031%2C%22east%22%3A-122.25136794042969%2C%22south%22%3A37.64872542852256%2C%22north%22%3A37.901641174768436%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

response = requests.get(url=url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")
address_list = []
link_list = []
price_list = []

# condtion: bool = len(price_list) > 0 and len(link_list) > 0 and len(address_list) > 0 and len(address_list) == len(
#     link_list) and len(link_list) == len(price_list)
condtion = True
while(condtion):
    price_list = soup.select(
        selector=".List-c11n-8-89-0__sc-1smrmqp-0.StyledSearchListWrapper-srp__sc-1ieen0c-0.kZyCWU.fgiidE.photo-cards li span[data-test='property-card-price']")
    address_list = soup.select(
        selector='.List-c11n-8-89-0__sc-1smrmqp-0.StyledSearchListWrapper-srp__sc-1ieen0c-0.kZyCWU.fgiidE.photo-cards li address[data-test="property-card-addr"]')
    link_list = soup.select(
        selector='.List-c11n-8-89-0__sc-1smrmqp-0.StyledSearchListWrapper-srp__sc-1ieen0c-0.kZyCWU.fgiidE.photo-cards li .StyledPropertyCardPhotoBody-c11n-8-89-0__sc-128t811-0.kVLKwo a')
    sleep(3)
    print("osama")
    if len(price_list) > 0 and len(link_list) > 0 and len(address_list) > 0 and len(address_list) == len(link_list) and len(link_list) == len(price_list):
        condtion =False

new_address_list = [n.text.split("|")[0] for n in address_list]
new_price_list = [n.text.split("+")[0].split("/")[0] for n in price_list]
new_link_list = []
for a in link_list:
    link = a["href"]
    if "https://www.zillow.com" not in link:
        new_link_list.append(f"https://www.zillow.com{link}")
    else:
        new_link_list.append(link)

pprint(new_address_list)
pprint(new_price_list)
pprint(new_link_list)

pprint(len(new_address_list))
pprint(len(new_price_list))
pprint(len(new_link_list))

# -----------------------------------------------------------------------------------------------#


chrome_driver_path = "C:\\Users\\Osama Raed Alnobani\\OneDrive\\Desktop\\development\\chromedriver_win32\\chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSd6uEYCnc5CmcCjUHcR-abRXxw74ZXw6gJrVY8vtLvAnAy3zw/viewform?usp=sf_linkhttps://docs.google.com/forms/d/e/1FAIpQLSd6uEYCnc5CmcCjUHcR-abRXxw74ZXw6gJrVY8vtLvAnAy3zw/viewform?usp=sf_link")
sleep(5)
for i in range(len(new_link_list)):
    address = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(new_address_list[i])

    sleep(2)
    price = driver.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(new_price_list[i])

    sleep(2)
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(new_link_list[i])

    sleep(2)
    send = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    send.click()

    sleep(5)

    again = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    again.click()
