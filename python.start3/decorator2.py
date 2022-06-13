# def testFac(base):
#     def testDoc(callback):
#         def innerFunc():
#             result = base*3
#             print("Doc", base)
#             callback(result)
#         return innerFunc
#     return testDoc

# @testFac(3)
# def decoratorFunc(result):
#     print("normal func", result)

# decoratorFunc()


def decocal(base):
    def calculator(callback):
        def run():
            total = 0
            for i in range(1,base+1):
                total += i
            # 把計算結果透過參數傳到被裝飾的普通函式中
            callback(total)
        return run
    return calculator

@decocal(100)
def test(n):
    print("result is: ", n)

@decocal(50)
def show(n):
    print("結果是", n)

test()
show()