# 實體物件的設計 : 平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # 定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return ((self.x- targetX)**2+ (self.y-targetY)**2)**0.5
# 建立第一個實體物件
p1= Point(1,5)
# 建立第二個實體物件
p2= Point(3,4)
# print(p1.x,p1.y)
# print(p2.x,p2.y)

# 呼叫實體方法 / 函式
# p1.show()
# result= p1.distance(0,0)
# print(result)
# p2.show()
# result2= p2.distance(0,0)
# print(result2)


class FullName:
    def __init__(self,first,last):
        self.first= first
        self.last= last
name1 = FullName("HsuanMing", "Chi")
name2= FullName("WeiChu", "Liao")
# print(name1.first, name1.last)
# print(name2.first, name2.last)

## File 實體物件操作
class File:
    def __init__(self, name):
            self.name= name
            self.file= None # 尚未開啟檔案 初期是none
    def open(self):
        self.file= open(self.name, mode= "r", encoding= "utf-8")
    def read(self):
        return self.file.read()

f1= File("data.txt")
f1.open()
data= f1.read()
print(data)

f2= File("data_company.txt")
f2.open()
data2= f2.read()
print(data2)