from numpy import broadcast
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\karak\\OneDrive\\Masaüstü\\chromedriver")

driver.get("http://yaz.tf.firat.edu.tr/")

duyuru = driver.find_elements(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]")

duyuruListesi = []

for i in duyuru:
    duyuruListesi.append(i.text)

with open("duyuru.txt","w",encoding="utf-8") as file:
    for i in duyuruListesi:
        file.write(i)


time.sleep(3)
driver.quit()