# For CIS 4150: Software Reliability and Testing
# Assignment 3 Part 2
# By Ian McKechnie
# Friday, November 11, 2022

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "./chromedriver"

def automator():
    driver = webdriver.Chrome(PATH)

    driver.get("https://techwithtim.net")

    print("Title of the driver: " + driver.title)

    search = driver.find_element(By.NAME, "s")
    search.send_keys("test")
    search.send_keys(Keys.RETURN)
    print("Successfully search for keyword 'test'")

    header = driver.find_element(By.ID, "menu-item-2262")
    header.click()
    print("Successfully clicked on the 'Gear page' header")

automator()