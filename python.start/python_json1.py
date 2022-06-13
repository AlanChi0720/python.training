# file = open("data.txt", mode="w", 
# encoding="utf-8") # utf-8 可中文
# file.write("Hello File\nSecond line\n中文")
# file.close()

# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("5\n3")

# sum= 0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for i in file:
#         sum += int(i)
# print(sum)

import json
#從檔案中讀取json 放入變數data
with open("config.json", mode= "r" ) as file:
    data= json.load(file)
print(data) # json 資料是字典
# print("name:", data["name"])
# print("version:", data["version"])
data["name"] = "Alan" # 修改變數中的資料
# 把最新的資料寫回json中
with open("config.json", mode= "w" ) as file:
    json.dump(data, file)