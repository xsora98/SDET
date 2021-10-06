from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import sys
import time

driver = webdriver.Chrome()
driver.get("https://www.bayut.com")

print("Moving to Popular Searches...")
try:
    ActionChains(driver).move_to_element(driver.find_element_by_xpath('//div[text()="Popular searches in the UAE"]')).perform()
    driver.find_element_by_xpath('//div[text()="To Rent"]').click()
    time.sleep(1)
except NoSuchElementException:
    print("The Popular Searches could not be found")
    driver.quit()
    sys.exit(1)

print("Expanding Popular Searches...")
try:
    main=driver.find_element_by_class_name("fc910dcd")
    el=main.find_elements_by_class_name("_2f838ff4")
    for x in el:
        x.click()
except NoSuchElementException:
    print("The Popular Searches could not be found")
    driver.quit()
    sys.exit(1)

print("Creating the Dubai Apartments list from Popular Searches...")
try:
    list=main.find_elements_by_class_name("_5a12e6f6")
    for x in list:
        if x.find_element_by_class_name("_78d325fa ").text=="Dubai Apartments":
            list_apartments=x.find_elements_by_class_name("_76ddbf32")
except NoSuchElementException:
    print("The Dubai Apartments field could not be found")
    driver.quit()
    sys.exit(1)

print("Preparing verify and link lists...")
try:
    list_verify=[]
    for x in list_apartments:
        if "-" in x.text:
            list_verify.append(x.text.replace("- ","("))
        else:
            list_verify.append(x.text)
    list_links=[]
    for x in list_apartments:
        link=x.find_element_by_css_selector("a").get_attribute("href")
        list_links.append(link)
except NoSuchElementException:
    print("The links could not be found")
    driver.quit()
    sys.exit(1)

print("Verify if the search is correct...")
try:
    verify=0
    i=0
    for x in list_links:
        driver.get(x)
        src_header=driver.find_element_by_id("search-header")
        if("Apartments for rent in "+list_verify[i] in src_header.text):
            verify=verify+1
            i=i+1
        else:
            print(list_verify[i])

except NoSuchElementException:
    print("The search field could not be found")
    driver.quit()
    sys.exit(1)

if verify==len(list_verify):
    print("Test passed")
else:
    print("Test failed")

driver.quit()