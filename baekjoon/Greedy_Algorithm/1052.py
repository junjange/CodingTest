import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0

#  bin(n).count('1') => 물병의 개수
# 물병의 개수가 k개보다 클 때까지 반복
while bin(n).count('1') > k:
    # 1L 물 구입
    n += 1 
    cnt += 1

# 구매한 물통의 개수 출력
print(cnt)
