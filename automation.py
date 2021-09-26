#Basic from and import commands to run the code properly.These commands are necessary.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#Give a valid input
search= input("Type to search a topic:")

#Set the executable path location of chromedriver.exe in your computer
driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.implicitly_wait(10)

driver.maximize_window()

driver.get(f"https://wikipedia.org")

driver.find_element_by_name("search").send_keys(search)


driver.find_element_by_css_selector("#search-form > fieldset > button > i").click()

WebDriverWait(driver,10)

result= driver.find_elements_by_tag_name("p")

notepad =open(search,'w+')

for results in result:
 final= (results.text)
 print(final)
 textfile = final
 notepad.writelines(textfile)

notepad.close()


driver.close()
