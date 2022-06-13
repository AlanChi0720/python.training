import urllib.request as request

#取得NTU 網站的原始碼(HTML, css, js)
# src = "https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8") 

import json
src ="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)

# 公司名稱 -> 列表
clist = data["result"]["results"]
# 將整理出的資料放入檔案中
with open("data_company.txt", mode= "w", encoding= "utf-8") as file:
    for i in clist:
        file.write(i["公司名稱"]+"\n")