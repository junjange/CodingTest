# 아이디어
# 동전은 큰 수부터 더한다.


n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)

count = 0

for i in range(len(coin)):

    if coin[i]<=k:
         num = k // coin[i]
         k -= num * coin[i]
         count+=num
    if k==0:
        break


print(count)


