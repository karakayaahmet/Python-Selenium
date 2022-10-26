from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\karak\\OneDrive\\Masaüstü\\chromedriver")

driver.get("https://diziyleogren.com/blog/ingilizce-dizi-ve-filmlerde-en-sik-kullanilan-5000-kelime")

kelime = driver.find_elements(By.XPATH, "/html/body/div/div/div[1]/div/table/tbody")

kelimeler = []

for i in kelime:
    kelimeler.append(i.text)

with open("kelimeler.txt","w",encoding="utf-8") as file:
    for i in kelimeler:
        file.write(i+"\n")

time.sleep(3)

driver.quit()
