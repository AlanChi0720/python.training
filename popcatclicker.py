from selenium import webdriver # 先在TERMINAL "pip install selenium"
import time

PATH="D:/chromedriver.exe"
driver=webdriver.Chrome(PATH)
url='https://popcat.click/'
driver.get(url)
cat=driver.find_element_by_id('app')
while True:
  for i in range(10000): #(輸入想要點的次數) 但在while 迴圈中 所以意義不大
    cat.click()
  time.sleep(2) # 當點完(次數) 休息幾秒繼續點