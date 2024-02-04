import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



import requests


import urllib.request


def read_full_page(link):
    
    browser.get(link)
    time.sleep(10)
    continue_button = browser.find_element(By.TAG_NAME,"button")
    print(continue_button.text)
    
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.get("https://finance.yahoo.com/topic/stock-market-news")
print("Got 1")
time.sleep(10)

elem = browser.find_element(By.TAG_NAME,"body")




no_of_pagedowns = 1000

while no_of_pagedowns:
    
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
    
post_elems = browser.find_element(By.ID,"Fin-Stream")

base_dir = "C:/CodeV/webscrapper/download"

t=time.localtime()
current_time = time.strftime("%H_%M_%S",t)
print(current_time)

os.chdir(base_dir)


a_list = post_elems.find_elements(By.TAG_NAME,"a")
count = 0
for a in a_list:
    try:
        link = a.get_attribute("href")
        if "finance.yahoo.com" in link:
            count+=1
            print(link)
            time.sleep(1)
            #response = urllib.request.urlopen(link,timeout=10)
            html = requests.get(link).text
            #html = response.read().decode()

            #print(html)
            with open(f"Count-{count}.html","w", encoding="utf-8") as output:
                output.write(html)
                print("done")
            
            #read_full_page(link)
    except:
        print(f"{count} failed")
        
print(count)

    