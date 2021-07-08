import sys

n, k = map(int, sys.stdin.readline().split())
# 공차가 1인 등차수열의 합
basket = k * (k + 1) // 2
# 공차가 1인 등차수열의 합보다 공의 개수가 작으면 나눠 담을 수 없다.
if n < basket:
    print(-1)
else:
    # 공에서 공차가 1인 등차수열의 합을 뺀 값이 k의 배수이면 최소 공의 개수 차이는 k-1이 된다.
    if (n - basket) % k == 0:
        print(k - 1)
    # k의 배수가 아니면 최소 공의 개수 차이는 k가 된다.
    else:
        print(k)
