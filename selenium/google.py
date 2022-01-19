from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import Request, urlopen
import time
import urllib.request

opener=urllib.request.build_opener()

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]

urllib.request.install_opener(opener)
driver = webdriver.Chrome(executable_path='E:\python\selenium\chromedriver.exe')
driver.get("https://www.google.co.jp/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("조코딩")
elem.send_keys(Keys.RETURN)
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
time.sleep(3)
imgUrl=driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
urllib.request.urlretrieve(imgUrl, "test.jpg")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()