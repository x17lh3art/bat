from selenium import webdriver
import os
import time

useragent = "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/71.0"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--allow-popups-during-page-unload")
chrome_options.add_argument("--disable-background-timer-throttling")
chrome_options.add_argument(f'user-agent={useragent}')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

driver.get("https://b1bat.blogspot.com/")
print("Buffering")
driver.find_element_by_link_text("Batting").click()
time.sleep(5)
driver.find_element_by_link_text("further").click()
print("Triggering")
time.sleep(1700)

driver.quit()

print("Great....")
