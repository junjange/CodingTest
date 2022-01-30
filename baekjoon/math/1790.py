import sys

n, k = map(int, sys.stdin.readline().split())
ans = 0
num = 1
nine = 9


# 반복문을 통해 자리수에 맞게 수를 빼준다.
while k > num * nine:
    k -= (num * nine) # 1의 자리는 9개 10의 자리는 18개..
    ans += nine # 현재 수

    # 자리수 이동
    num += 1
    nine = nine * 10

# 남은 자리수의 수를 현재 수에 더해준다.
ans = (ans+1) + (k-1) // num

if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1) % num])
