# if
# x = int(input('please insert your number: '))
# if x > 200: 
#     print('bigger than 200')
# elif x >100:
#     print('bigger than 100 and smaller than 200')
# else:
#     print(" smaller than 100")

n1 = int(input("please insert number1: "))
n2 = int(input("please insert number2: "))
op= input('please insert operation (+,-,*,/): ')
if op == "+":
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == "/":
    if n2 != 0:
        print(n1/n2)
    else:
        print("stupid")
else:
    print("fuck off")