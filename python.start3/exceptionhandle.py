while True:
    data = input("Please enter number: ")
    try:
        number = int(data)
        break
    except Exception:
        print("Re-enter")
        
number = number * 2
print(number)