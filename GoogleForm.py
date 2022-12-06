from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfPX1BCRblqSzuSvMxNAlnVaHwp0Jb0NaL3_BRfY6f4-sQhrw/viewform")
time.sleep(2)

checkbox = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label')
textbox = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
checkboxtwo = browser.find_element(By.XPATH,'//*[@id="i22"]/div[3]/div')
submit = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

checkbox.click()

names = "Jake and Mary"
textbox.send_keys(names)

checkboxtwo.click()

time.sleep(5)

submit.click()