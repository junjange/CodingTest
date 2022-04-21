import sys


n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
a, b = divmod(sum(h), 3) # 몫, 나머지
cnt = 0

# 모든 나무의 합을 3으로 나누었을 때 0이 되지 않으면
# 물뿌리개를 통해 만들 수 없는 높이인 것이다.
if b == 0:
    # 반복문을 통해 2의 물뿌리개의 횟수를 구한다.
    for i in h:
        cnt += i // 2

    # 2의 물뿌리개의 횟수가 3으로 물을 뿌린 횟수보다 크다면
    # 원하는 높이의 나무를 만들 수 있다.
    if cnt >= a:
        print("YES")

    else:
        print("NO")

else:
    print("NO")
