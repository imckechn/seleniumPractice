# For CIS 4150: Software Reliability and Testing
# Assignment 3 Part 3
# By Ian McKechnie
# Friday, November 18, 20222

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

PATH = "./chromedriver"
URL = "https://hellomeal.com/menu/"

def setUp(url):
    driver = webdriver.Chrome(PATH)

    driver.get(url)
    print(driver.title)

    return driver

def selectByClass(driver, str):
    elem = driver.find_element(By.CLASS_NAME, str)
    elem.click()
    print("Success")

def selectByName(driver, str):
    elem = driver.find_element(By.NAME, str)
    elem.click()
    print("Success")


def searchFor(driver, arg):
    search = driver.find_element(By.NAME, "s")
    search.send_keys(arg)
    search.send_keys(Keys.RETURN)

def selectByXPath(driver, path, index):
    elem = driver.find_elements(By.XPATH, path)
    #print("num elems found: " + str(len(elem)))
    elem[index].click()

print("Opening browser and website")
driver = setUp(URL)

print("Filtering to only AMRITSAR KITCHEN")
selectByXPath(driver, '//*[@id="post-6734"]/div/div/section/div/div[1]/div/div/div/div[2]/div[2]/ul/li', 0)
time.sleep(5)
print("Success\n")

print("Opening First product")
selectByXPath(driver, '//*[@id="post-6734"]/div/div/section/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li[2]/a[1]', 0)
print("Success\n")

print("Adding to cart")
selectByName(driver, "add-to-cart")
print("Success\n")

print("Going back to menu")
selectByXPath(driver, '//*[@id="menu-item-6743"]/a', 0)
print("Success\n")


print("Filtering to only show animal meat based proteins")
selectByXPath(driver, '//*[@id="post-6734"]/div/div/section/div/div[1]/div/div/div/div[2]/div[4]/ul/li[1]', 0)
time.sleep(5)
print("Success\n")

print("Adding the chicken curry to cart (Or whatever element is first in the list, it changes depending on the day")
selectByXPath(driver, '//*[@id="post-6734"]/div/div/section/div/div[2]/div/div/div/div[1]/div[2]/div/div/ul/li/a[2]', 0)
print("Success\n")

print("Going to cart")
selectByClass(driver, 'cart-container')
print("Success")
