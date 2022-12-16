# For CIS 4150: Software Reliability and Testing
# Assignment 3 Part 3
# By Ian McKechnie
# Friday, November 18, 2022

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "./chromedriver"
URL = "https://techwithtim.net"

def setUp(url):
    driver = webdriver.Chrome(PATH)

    driver.get(url)
    print(driver.title)

    return driver



def searchFor(driver, arg):
    search = driver.find_element(By.NAME, "s")
    search.send_keys(arg)
    search.send_keys(Keys.RETURN)


driver = setUp(URL)

print("Using the search function on the Techwithtim website")
print("Serching for 'Hello world'")
searchFor(driver, "Hello world")
print("Success")

print("Searching for 'Chadha'")
searchFor(driver, "Chadha")
print("Success")

print("Searching for 'Can I get 100% on this assignment?'")
searchFor(driver, "Can I get 100% on this assignment?")
print("Success")