import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import random as rd

#specify start and end pages
start = 1 
end = 100

url = "https://www.seloger.com/list.htm?projects=2%2C5&types=1%2C2&natures=1%2C2%2C4&places=%5B%7Bci%3A750056%7D%5D&enterprise=0&qsVersion=1.0&LISTING-LISTpg="

option = webdriver.ChromeOptions()
option.add_argument(' — incognito')

driver = webdriver.Chrome(executable_path='D:/OneDrive/SIMPLON/Subprimers/Scrap/chromedriver.exe')

driver.maximize_window()

df = pd.DataFrame(columns = ['price', 'rooms', 'bedrooms', 'surface', 'district', 'text', 'plus', 'general', 'inside', 'others'])

def slp():

    return time.sleep(rd.randint(1,2) + rd.random())

slp()

for n in range(start,end):

    driver.get(url + str(n))

    adds = driver.find_elements_by_name("classified-link")
    hrefs = [href for href in [element.get_attribute("href") for element in adds] if href.startswith('https://www.seloger.com/annonces/achat/appartement/')]

    for href in hrefs:

        print(href)
        driver.get(href)

        try:

            price = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div[2]/div[2]').text
            rooms = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div[2]/div[3]/div[1]/div[2]').text
            bedrooms = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div[2]/div[3]/div[2]/div[2]').text
            surface = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div[2]/div[3]/div[3]/div[2]').text
            district = driver.find_element_by_xpath('//*[@id="top"]/div[2]/div[2]/div[1]/div[2]').text

            slp()

            driver.find_element_by_xpath('//*[@id="showcase-description"]/div[1]/div/div/div/div[2]').click()
            text = ' '.join([element.text for element in driver.find_element_by_xpath('//*[@id="showcase-description"]/div[1]/div/div/div/div[1]').find_elements_by_tag_name('p')])

            slp()

            driver.find_element_by_xpath('//*[@id="showcase-description"]/div[2]/div[2]/div[2]').click()
            plus = [element.text for element in driver.find_element_by_xpath('//*[@id="showcase-description"]/div[2]/div[1]/div').find_elements_by_tag_name('figcaption')]
            general = [element.text for element in driver.find_element_by_xpath('//*[@id="showcase-description"]/div[2]/div[2]/div[1]/div[1]').find_elements_by_tag_name('li')]
            inside = [element.text for element in driver.find_element_by_xpath('//*[@id="showcase-description"]/div[2]/div[2]/div[1]/div[2]').find_elements_by_tag_name('li')]
            others = [element.text for element in driver.find_element_by_xpath('//*[@id="showcase-description"]/div[2]/div[2]/div[1]/div[3]').find_elements_by_tag_name('li')]
            
            print([price, rooms, bedrooms, surface, district, text, plus, general, inside, others])
            df = df.append({'price':price, 'rooms':rooms, 'bedrooms':bedrooms, 'surface':surface, 'district':district, 'text':text, 'plus':plus, 'general':general, 'inside':inside, 'others':others}, ignore_index=True)
            
            print(n)

            slp()

            df.to_csv('data.csv',sep=';')

        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.ElementClickInterceptedException):

            continue
    
    n +=1