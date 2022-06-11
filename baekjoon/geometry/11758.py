import sys

p = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]


v1 = [p[1][0] - p[0][0], p[1][1] - p[0][1]] # p1 -> p0
v2 = [p[2][0] - p[1][0], p[2][1] - p[1][1]] # p2 -> p1
func = v1[0] * v2[1] - v1[1] * v2[0] # 벡터 외적

# 외적이 양수이면 sin < 180
if func > 0:
    print(1)

# 외적이 양수이면 sin > 180
elif func < 0:
    print(-1)

# 외적이 양수이면 sin == 180
else:
    print(0)
