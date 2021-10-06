from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import sys
import time

driver = webdriver.Chrome()
driver.get("http://www.bayut.com")

print("Select the apartments available for buying...")
time.sleep(1)
try:
    driver.find_element_by_class_name("e7c6503c").click()
    driver.find_element_by_xpath('//button[text()="Buy"]').click()
except NoSuchElementException:
    print("The Buy button could not be found")
    driver.quit()
    sys.exit(1)
    
print("Search for Dubai Marina...")
try:
    driver.find_element_by_class_name("a41c4dcc").send_keys("Dubai Marina")
    time.sleep(1)
except NoSuchElementException:
    print("The Search field could not be found")
    driver.quit()
    sys.exit(1)

print("Find apartments for specified criteria...")
try:
    driver.find_element_by_class_name("_0e756b14").click()
    driver.find_element_by_xpath('//a[text()="Find"]').click()
    time.sleep(1)
except NoSuchElementException:
    print("The Find button could not be found")
    driver.quit()
    sys.exit(1)

try:
    main=driver.find_element_by_class_name("bbfbe3d2")
    time.sleep(1)
    elements=main.find_elements_by_tag_name("article")
    time.sleep(1)
except NoSuchElementException:
    print("The articles could not be found")
    driver.quit()
    sys.exit(1)

nr=0
print("Verify if the results are correct...")
for x in elements:
    if "Dubai Marina" in x.find_element_by_class_name("d6e81fd0").text:
        nr=nr+1
if(nr==len(elements)):
    print("Test passed")
else:
    print("Test failed")

driver.quit()