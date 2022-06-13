# def test(arg):
#     arg(50) #呼叫回乎函式
#     arg("hello")

# def handle(data):
#     print(data)

# test(handle)



def add(n1,n2,cb):
    cb(n1+n2)

# 結果交給回乎函式 用於產生不同結果
def handle1(result):
    print("result is: ",result)

def handle2(result):
    print("結果是: ", result)

add(3,4,handle1)
add(5,6,handle2)