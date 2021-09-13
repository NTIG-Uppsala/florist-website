from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("http://www.itgwebb.se/klass/webb2/christoffer/florist-celeber/")

def testTitleName(titlename):
    assert titlename in driver.title

def checkForText(text):
    assert text in driver.find_element_by_xpath("/html/body").text

def checkForAddress():
    checkForText("Fjällgatan 32H")
    checkForText("981 39")
    checkForText("Kiruna")


testTitleName("Florist Celeber")
checkForAddress()

time.sleep(2)
driver.close()
