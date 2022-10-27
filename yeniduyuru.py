from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\Users\karak\\OneDrive\\Masaüstü\\chromedriver")

driver.get("http://yaz.tf.firat.edu.tr/announcements-detail/16775")

duyuru = driver.find_elements(By.XPATH,"/html/body/div[4]/div[1]/div[2]")

duyuru_metin = []

for i in duyuru:
    duyuru_metin.append(i.text)

with open("duyurular.txt","w",encoding="utf-8") as file:
    for i in duyuru_metin:
        file.write(i+"\n")

time.sleep(3)

driver.quit()