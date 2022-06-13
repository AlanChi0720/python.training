# 抓取 KKday 
import urllib.request as req
# 開發者工具 > Network > XHR/ preview 搜尋真url
url= "https://www.kkday.com/en-us/home/ajax_get_homepage_setting?csrf_token_name=a7367cb46aa86735472c1a8e499ea189"
# 建立 request物件 附加request headrs 的資訊
request= req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
})
with req.urlopen(request) as response:
    data= response.read().decode("utf-8") # 根據觀察 取得JSON的格式

# 解析JSON資料 取得標題
import json
# data = data.replace("", "") data如果有非JSON 形式 先清除
data = json.loads(data) # 把JSON資料解析成字典/列表的形式
posts = data["data"]["top_products"]["prod_list"]
for post in posts:
    # post = posts["name"]
    print(post["name"])
    # print(key)