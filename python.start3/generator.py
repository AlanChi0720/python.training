# def test():
#     print("stage 1")
#     yield 3
#     print("stage 2")
#     yield 5

# data = test()
# # print(data)

# for i in data:
#     print(i)

def even(max):
    number = 0
    while max >= number:
        yield number 
        number +=2

even = even(60)

for data in even:
    print(data)