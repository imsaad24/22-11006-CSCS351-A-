from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


web = webdriver.Chrome(ChromeDriverManager().install())
web.get('https://www.daraz.pk/')

FirstName = "Printed Summer Dress"
first = web.find_element_by_xpath('//*[@id="q"]')
first.send_keys(FirstName)

Submit = web.find_element_by_xpath('//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button')
Submit.click()

img = web.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div/[1]/div/a[1]/img')
img.click()
