# def solution(n):
#     sum = 0
#     for i in range(1, len(str(n))+1):
#         sum += n % 10
#         n = n//10
#     return sum

def solution(n):
    sum = 0
    while len(str(n)) > 0:
        if n > 0:
            sum += n % 10
            n = n // 10
        else:
            break
    return sum

def solution(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

solution(345)