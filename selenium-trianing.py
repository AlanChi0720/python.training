from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# settting Chrome Driver execute path
options = Options()
options.chrome_executable_path = "D:\pyhton.training\training_Flask\runtime.txt"

driver = webdriver.Chrome(options = options)
driver.maximize_window() # full screen website
driver.get("https://www.google.com.tw/webhp?hl=zh-TW&tab=ww")
driver.save_screenshot('screenshot-google.png')
driver.close()