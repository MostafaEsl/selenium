from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver_path = r"E:\course\python\chromedriver.exe" 

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

with webdriver.Chrome(service=Service(driver_path), options=options) as driver:
    driver.get(url)
    time.sleep(5)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[4]/div[1]/header/div[2]/a/button')
    element.click()
    time.sleep(10)
    input_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/form/label/div/div/input")
    input_element.send_keys("mostafaesl76@gmail.com")
    input_element.send_keys(Keys.ENTER)
    
    time.sleep(5)
    input_element1 = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/form/label/div/div[1]/input")
    input_element1.send_keys("10152099Most@f@")
    
    input_element1.send_keys(Keys.ENTER)
    time.sleep(5)
    element2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[2]/div/div/div[2]/div[1]/div[2]/a/div')
    element2.click()
    time.sleep(20)


