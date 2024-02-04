import time
import os
from pathvalidate import sanitize_filename

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



import requests


import urllib.request



base_dir = "C:/CodeV/webscrapper/download"
os.chdir(base_dir)

def read_full_page(link):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    time.sleep(2)
    continue_button = browser.find_elements(By.TAG_NAME,"button")
    print("reading from browser")
    print(len(continue_button))
    for button in continue_button:
        if button.get_attribute("class") == "link caas-button collapse-button":
            print(button.text)
            button.click()
            time.sleep(2)
            title = sanitize_filename(browser.title)
            print("Title -> " + title)
            print(f"{title} -> {sanitize_filename(title)}\n")
            article = browser.find_element(By.TAG_NAME,"article").text
            #print(browser.find_element(By.TAG_NAME,"article").text)
            
            with open(f"{title}.txt","w", encoding="utf-8") as output:
                output.write("Title :" +  title + " Article : " + article )
                print("done")
    browser.close()
    
#get file list from OS folder
file_path= "C:/CodeV/webscrapper/download/*.html"

import glob
print(glob.glob(file_path))

file_list = glob.glob(file_path)

for file in file_list:
    #f=open(file)
    #txt = f.read()
    #print(f"Contents of {file}")
    #print(txt)
    read_full_page(file)





    