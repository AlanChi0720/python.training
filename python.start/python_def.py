# def add(n1,n2):
#     result= n1+n2
#     return result
# value= add(3,4)
# print(value)

# def calculator(max):
#     sum=0
#     for i in range(1, max+1):
#         sum += i
#     return sum
# v1= calculator(10)
# v2= calculator(20)
# print(v1,v2)

# def power(base, exp=0):
#     print(base**exp)
# power(3,2)
# power(4)

# def devide(n1,n2):
#     print(n1/n2)
# devide(2,4)
# devide(n2=2,n1=4)

def avg(*n):
    sum=0
    for i in n:
        sum= sum+i
    print(sum/len(n))

