import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\karak\\OneDrive\\Masaüstü\\chromedriver")

driver.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=")

icerik = []

icerikler = []

bas = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/ul/li[3]/a", value="button")
bas.click()

# while By.CLASS_NAME != "page-link disabled":
#     icerik += driver.find_elements(By.CSS_SELECTOR,"body > div.wrapper > div.container.test-site > div > div.col-md-9 > div")
#     for i in icerik:
#         icerikler.append(i.text)
  

# with open("içerikler.txt","w",encoding="utf-8") as file:
#     for i in icerikler:
#         file.write(i)

time.sleep(3)

driver.quit()