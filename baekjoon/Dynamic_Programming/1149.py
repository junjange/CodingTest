import sys

n = int(sys.stdin.readline())
rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 반복문을 통해 각 집의 색을 칠할 수 있는 최소 비용에 경우의 수를 구한다.
for i in range(n - 1):
    rgb[i + 1][0] = min(rgb[i][1], rgb[i][2]) + rgb[i + 1][0] # 이전 집에 빨간색을 칠한 경우
    rgb[i + 1][1] = min(rgb[i][0], rgb[i][2]) + rgb[i + 1][1] # 이전 집에 초록색을 칠한 경우
    rgb[i + 1][2] = min(rgb[i][0], rgb[i][1]) + rgb[i + 1][2] # 이전 집에 파란색을 칠한 경우

# 마지막 집까지 색칠한 후 비용의 최솟값을 출력
print(min(rgb[n - 1]))
