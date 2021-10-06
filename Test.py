from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://www.bayut.com")

time.sleep(1)
driver.find_element_by_class_name("e7c6503c").click()
driver.find_element_by_xpath('//button[text()="Buy"]').click()

driver.find_element_by_class_name("a41c4dcc").send_keys("Dubai Marina")
time.sleep(1)
driver.find_element_by_class_name("_0e756b14").click()
driver.find_element_by_xpath('//a[text()="Find"]').click()

time.sleep(2)
main=driver.find_element_by_class_name("bbfbe3d2")
time.sleep(1)
elements=main.find_elements_by_tag_name("article")
time.sleep(1)
nr=0
for x in elements:
    if "Dubai Marina" in x.find_element_by_class_name("d6e81fd0").text:
        nr=nr+1
if(nr==len(elements)):
    print("Test 1 passed")
else:
    print("Test 1 failed")

driver.quit()