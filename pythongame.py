from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By

path="D:/python/chromedriver.exe"
driver=webdriver.Chrome(path)
url="https://tsj.tw/"
driver.get(url)
actions= ActionChains(driver)

blow = driver.find_element_by_id('click')
blow_count=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')

items = []
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))

prices = []
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))

# 點馬上吹
for i in range(10000):
    actions.click(blow)
    count=int(blow_count.text.replace("您目前擁有","").replace("技術點",""))
    for j in range(3):
        price=int(prices[j].text.replace("技術點",""))
        if count >= price:
            upgrade_actions= ActionChains(driver)
            upgrade_actions.move_to_element(items[j])
            upgrade_actions.click()
            upgrade_actions.perform()
            break