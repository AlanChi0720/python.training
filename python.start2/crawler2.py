import urllib.request as req

def getdata(url):
    # 建立 request物件 附加request headrs 的資訊
    request= req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data= response.read().decode("utf-8")

    # 解析原始碼 取得標題
    import bs4
    root= bs4.BeautifulSoup(data, "html.parser") # bs4解析HTML
    titles= root.find_all("div", class_="title") # class_"title 的div 標籤
    for title in titles:
        if title.a != None: # 如果有包含 a 標籤
            print(title.a.string)
    # 抓到上頁網址
    nextlink= root.find("a",string="‹ 上頁") # 找到內文是‹ 上頁的a 標籤
    return nextlink["href"]

pageurl= "https://www.ptt.cc/bbs/Gossiping/index.html"
count= 0
while count<5:
    pageurl = "https://www.ptt.cc"+getdata(pageurl)
    count +=1