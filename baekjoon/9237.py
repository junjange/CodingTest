import sys

n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
# 묘목이 제일 오래 걸리는 것부터 심는다.
t.sort(reverse= True)
# 반복문을 통해 묘목이 자라는 시간에 묘목을 심는데 걸리는 시간을 더해준다.
for i in range(n):
    t[i] += i
# 묘목이 자라는데 제일 오래 걸리는 시간 + 묘목을 구입한 날과 이장님을 초대하는 날을 출력한다.
res = max(t) + 2
print(res)
