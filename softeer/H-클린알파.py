import sys

p, n = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

# 처음 바이러스를 변수 안에 넣는다.
# 1초때 침입한 바이러스
result = a[0]

# 2초부터 n초만큼 반복한다.
for i in range(1, n):
    # result에 바이러스 증가율를 곱해주고 1000000007로 나눈 나머지를 넣는다.
    result = (result * p) % 1000000007
    # 초가 지날수록 바이러스가 침입하기때문에 바이러스를 더해준다.
    result += a[i]

# 총 바이러스 개수 출력
print(result)
