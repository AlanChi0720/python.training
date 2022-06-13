# # 定義裝飾器
# def myDeco(callback):
#     def run():
#         print("code in deco")
#         callback(1) # 被裝飾的函式
#     print(callback)
#     return run

# # 使用裝飾器
# @myDeco # 帶有裝飾器
# def test(data):
#     print("normal code in func", data)

# test()

def calculator(callback):
    def run():
        result = 0
        for i in range(1,51):
            result += i
        # 把計算結果透過參數傳到被裝飾的普通函式中
        callback(result)
    return run

@calculator
def test(n):
    print("result is: ", n)

@calculator
def show(n):
    print("結果是", n)

test()
show()