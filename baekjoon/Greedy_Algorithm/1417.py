import sys

n = int(sys.stdin.readline())
# 다솜이의 투표수
target = int(sys.stdin.readline())
# 다른 후보들의 투표수
m = [int(sys.stdin.readline()) for _ in range(1, n)]
# 매수 횟수
buy = 0

# 후보가 1명이면 다솜이가 당선
if n == 1:
    print(0)
else:
    # 다른 후보들의 투표수를 내림차순하여 큰 투표수와 다솜이의 투표수를 비교한다.
    m.sort(reverse=True)
    # 다솜이의 투표수가 제일 클때까지 반복한다.
    # 다솜이의 투표수를 +1 하고 제일 큰 투표수를 -1 한다.
    # 매수 했으므로 매수를 카운트한다.
    while m[0] >= target:
        target += 1
        m[0] -= 1
        buy += 1
        # 다시 다른 후보들의 투표수를 내림차순하여 제일 큰 투표수와 비교한다.
        m.sort(reverse=True)
    print(buy)
