import sys

a, b = map(int, sys.stdin.readline().split())
temp = []
# 반복문을 통해 b구간까지의 수열을 만든다.
for i in range(1, b + 1):
    for j in range(i):
        temp.append(i)

# 만든 수열의 a부터 b구간까지 더한 값을 출력
print(sum(temp[a - 1:b]))
