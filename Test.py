#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver import ActionChains

from waybackpy import Url

import datetime

import matplotlib.pyplot as plt


# In[2]:


def noClickYet(driver, url):

    driver.get(url)
    
    sleep(10)
    
    cookBeforeClick = driver.get_cookies()
    
    return cookBeforeClick


# In[3]:


def clickAcceptAll(driver, url):
    
    driver.get(url)
    driver.maximize_window()

    # Find and click ACCEPT ALL button.
    data = click_banner(driver)
    
    #Scrap cookies once they are collected by the website. 
    sleep(10)
    cookAfterAcceptAll = driver.get_cookies()
    
    return cookAfterAcceptAll


# In[4]:


def clickRejectAll(driver, url):
    
    driver.get(url)
    driver.maximize()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-cta-do-not-consent"))).click()

    sleep(10)
    
    cookAfterRejectAll = driver.get_cookies()
    
    return cookAfterRejectAll


# In[5]:


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
            if element.text.lower().strip(" ✓›!\n") in accept_words_list:
                print(element.text)
                print("and here")
                #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, driver.get(element)))).click()
                element.click()
                return {'successful': True, 'error': 'none' }
        except Exception as e:
            print("Failed", e)
            return {'successful': False, 'error': 'click_error' }
    #return {'successful': False, 'error': 'no_accept_button' }
    print("No accept button")


# In[5]:


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0"
github_url = "https://github.com/"

github_wayback_obj = Url(github_url, user_agent)

# list of urls for the website for each month
github_url_dates =[]

# iterating between 01-07-2019 to 25-03-25 by jumps of 31 days 
start_date = datetime.date(2019,7,1)
end_date = datetime.date(2021,3,25)
delta = datetime.timedelta(days=31)

while start_date <= end_date:
    #print(start_date)
    # sometimes the API fails so in that case we simply try again
    try:
        github_url_dates.append(github_wayback_obj.near(year=start_date.year, month=start_date.month).archive_url)
        start_date += delta
    except:
        continue


# In[6]:


github_url_dates


# In[15]:


url = 'https://www.youtube.com'
options = FirefoxOptions()
#options.headless = True
service = FirefoxService(r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver = webdriver.Firefox(service=service, options=options)

user_option = ['NOTHING', 'ACCEPT', 'REJECT']
GLOBAL_SELECTOR = "a, button, div, span, form, p"

#driver.get(url)

def main():
    
    for url in github_url_dates:

    #none = noClickYet(driver, url)
    
        allCookies = clickAcceptAll(driver, url)
        print(len(allCookies))
        
    #noneCookies = clickRejectAll(driver, url)
    #print(len(none), len(allCookies), len(noneCookies))
    # print(len(none), len(noneCookies))
    
    # print(len(none), len(allCookies))
main()
driver.quit()


# In[9]:


from tranco import Tranco
t = Tranco(cache=True, cache_dir='.tranco')
latest_list = t.list()
date_list = t.list(date='2022-10-01')
latest_list.top(10000)
latest_list.list_id
latest_list.list_page
latest_list.rank("google.com")
#latest_list.rank("not.in.ranking") # returns -1


# In[25]:


filtered_french_websites = [k for k in date_list.list if '.fr' in k]
print(filtered_france)


# In[46]:


def click_bannere(driver):

    accept_words_list = set()
    for w in open("accept_words_languages.txt", "r").read().splitlines():
        if not w.startswith("#") and not w == "":
            accept_words_list.add(w)

    print(accept_words_list)
    banner_data = {"matched_containers": [], "candidate_elements": []}
    contents = driver.find_elements(By.CSS_SELECTOR,GLOBAL_SELECTOR)

    candidate = None
    
    for c in contents:
        if c.text.lower().strip(" ✓›!\n") in accept_words_list:
            candidate = c
            banner_data["candidate_elements"].append({"id": c.id,
                                                      "tag_name": c.tag_name,
                                                      "text": c.text,
                                                      "size": c.size,
                                                      })
            break
            
    # Click the candidate
# in some pages element is not clickable
        #log("Clicking text: {}".format (candidate.text.lower().strip(" ✓›!\n")) )
    
    if candidate is not None:
        
        candidate.click()
        banner_data["clicked_element"] = candidate.id
        #log("Clicked: {}".format (candidate.id) )

    return banner_data


# In[ ]:




