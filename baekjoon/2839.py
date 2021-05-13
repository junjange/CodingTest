n = int(input())

result = 0

while True:

    if(n % 5 == 0) :
        result = n // 5 + result
        print(result)
        break
    n -= 3
    result += 1

    if(n < 0) :
        print(-1)
        break
