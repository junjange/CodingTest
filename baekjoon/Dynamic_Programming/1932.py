import sys

n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 반복문을 통해 각 층을 확인한다.
for i in range(1, n):
    # 반복문을 통해 각 층의 수에 가중치를 준다.
    for j in range(len(m[i])):

        # 각 층의 왼쪽 줄일 때
        # 이전 층의 왼쪽 줄에 가중치를 더한다.
        if j == 0:
            m[i][j] += m[i - 1][j]

        # 각 층의 오른쪽 줄일 때
        # 이전 층의 오른쪽 줄에 가중치를 더한다.
        elif j == i:
            m[i][j] += m[i - 1][j - 1]

        # 각 층의 중간 줄일 때
        # 이전 층의 왼쪽 줄애 가중치와 오른쪽 줄에 가중치 중 큰 값을 더한다.
        else:
            m[i][j] += max(m[i - 1][j - 1], m[i - 1][j])

# 마지막 층에 최댓값을 출력
print(max(m[n - 1]))
