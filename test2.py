#!/usr/bin/env python
# coding: utf-8

# In[2]:


import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tranco import Tranco
import json
import waybackpy


# In[3]:


def cookies_before_click(driver, url):
    driver.get(url)

    sleep(10)

    cookies_before_click = driver.get_cookies()

    return cookies_before_click


# In[80]:


def cookies_before_and_after_accept(driver, url):
    driver.get(url)
    
    sleep(20)
    
    cookies_before_click = driver.get_cookies()
    
    print(click_banner(driver))
    
    sleep(10)
    
    cookies_accept_all = driver.get_cookies()
    
    return cookies_before_click, cookies_accept_all


# In[5]:


def cookies_accept_all(driver, url):
    driver.get(url)
    driver.maximize_window()

    # Find and click ACCEPT ALL button.
    click_banner(driver)

    #Scrap cookies once they are collected by the website. 
    sleep(10)
    cookAfterAcceptAll = driver.get_cookies()

    return cookies_accept_all


# In[6]:


def click_reject_all(driver, url):
    driver.get(url)
    driver.maximize()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-do-not-consent"))).click()

    sleep(10)

    click_reject_all = driver.get_cookies()

    return click_reject_all


# In[7]:


#https://github.com/marty90/priv-accept/blob/7c87be9441a6425160611d7fd91fd1e4ae7bceaf/priv-accept.py

def click_banner(driver):
    accept_words_list = set()
    for w in open("accept_words_languages.txt", "r", encoding="utf-8").read().splitlines():
        if not w.startswith("#") and not w == "":
            accept_words_list.add(w)

    sleep(20)
    content = driver.find_elements(By.CSS_SELECTOR, GLOBAL_SELECTOR)
    for element in content:
        try:
            if element.text.lower().strip(" ??????!\n") in accept_words_list:
                print(element.text)
                print("and here")
                #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, driver.get(element)))).click()
                element.click()
                return {'successful': True, 'error': 'none'}
        except Exception as e:
            print("Failed", e)
            return {'successful': False, 'error': 'click_error'}
    return {'successful': False, 'error': 'no_accept_button' }


# In[15]:


# Initializing tranco-list.eu list.
t = Tranco(cache=True, cache_dir='.tranco')
#latest_list = t.list()

# Get tranco list for the specific date
date_list = t.list(date=DATE_TRANCO_LIST)


# In[78]:


# Filter the list to what we are looking for.
french_websites = [web for web in date_list.list if '.fr' in web]
french_websites_www = [f'{website}' for website in french_websites]

first_three_websites = french_websites_www[0:NUMBER_OF_WEBSITES]

def waybackify_url(url, closest_timestamp):
    return f'https://web.archive.org/web/{closest_timestamp}/{url}'

loist = {}

import time 


for i in first_three_websites:
    loist2 = []
    start_date = START_DATE_FRANCE
    while start_date <= END_DATE_FRANCE:
        url = waybackify_url(i, to_integer(start_date))
        loist2.append((url, (start_date.year, start_date.month)))
        start_date += delta
    loist[i] = loist2

def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

#for el in list(base):
#    time.mktime(datetime.datetime.strptime(el, "%d/%m/%Y").timetuple())
    
print(loist)
#print(first_three_websites)


# In[111]:


def go_over_months(website):
    # create object from passed website
    wayback_obj = Url(website, USER_AGENT).save()
    print(website)
    print(wayback_obj)

    # list of urls for the website for each month
    urls_of_dates = []

    # iterating between 01-07-2019 to 25-03-25 by jumps of 31 days 
    start_date = START_DATE_FRANCE

    # append list of urls using wayback obect wuth specific date to interact with the API.
    while start_date <= END_DATE_FRANCE:
        # sometimes the API fails so in that case we simply try again
        try:
            urls_of_dates.append((wayback_obj.near(year=start_date.year, month=start_date.month).archive_url, (start_date.year, start_date.month)))
            print(urls_of_dates, "Success.")
            0# go to the next month
            start_date += delta
            # the API is rather slow so we need to give some time to rest (:
            sleep(3)
        except Exception:
            print(Exception)
            continue
    return urls_of_dates


# In[112]:


def go_over_websites(websites_list):
    # Create 2D list of all websites urls for each month 
    get_list = {}
    for url in websites_list:

        # 2D list
        get_list[url] = go_over_months(url)
        print(get_list)
        
    return get_list


# In[58]:


user_option = ['NOTHING', 'ACCEPT', 'REJECT', 'MANAGE']
GLOBAL_SELECTOR = "a, button, div, span, form, p"
NUMBER_OF_WEBSITES = 3

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
START_DATE_FRANCE = datetime.date(2020,7, 14)
END_DATE_FRANCE = datetime.date(2020, 12, 25)
delta = datetime.timedelta(days=31)

DATE_TRANCO_LIST='2022-10-01'


# In[114]:


dictory_of_urls = go_over_websites(first_three_websites)


# In[110]:


print(dictory_of_urls)


# In[61]:


with open("{}_all_urls.txt".format("Urls"), 'w') as outfile:
                json.dump(dictory_of_urls, outfile, indent = 4)


# In[79]:


#url = 'https://www.youtube.com'
options = FirefoxOptions()
#options.headless = True
service = FirefoxService(r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver = webdriver.Firefox(service=service, options=options)

def main():
    
    # Collect cookies for every month, write to two JSON files: before click and after ACCEPT ALL,
    # and return the number of cookies.
    for website in loist:
        
        website_name = website
        
        for url in loist[website]:
            
            print(website, url[1])
            
            # store cookies before and after click
            cookies_before, cookies_after = cookies_before_and_after_accept(driver, url[0])
            
            print(len(cookies_before), len(cookies_after))
            
            # create two JSON files
            with open("{}_cookies_no_click.json".format(website_name), 'a') as outfile:
                json.dump((url[1], cookies_before), outfile, indent = 4)
            with open("{}_cookies_after_click.json".format(website_name), 'a') as outfile:
                json.dump((url[1], cookies_after), outfile, indent = 4)

main()
driver.quit()


# In[147]:


import glob, os, os.path

mydir = r"V:\Uni\Thesis\Code\Thesis"
filelist = glob.glob(os.path.join(mydir, "*.JSON"))
for f in filelist:
    os.remove(f)


# In[126]:


for website in dictory_of_urls:
       website_name = website
       print(website)
       for url in dictory_of_urls[website]:
           print(url[1])


# In[142]:


dictorio = {}

dictory_of_urls


# In[104]:


print(dictory_of_urls)


# In[ ]:




