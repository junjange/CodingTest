import sys

n = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
# 상자안에 넣어진 상자의 계수
result = [1] * n

for i in range(1, n):
    # 상자의 계수를 비교할 변수 초기화
    result_max = 0
    for j in range(i):

        # 다음 상자의 크기와 그전에 있는 모든 상자의 크기 비교
        if box[i] > box[j]:
            # 상자의 계수 비교
            if result_max < result[j]:
                result_max = result[j]

    # 상자의 계수 카운트
    result[i] = result_max + 1

# 리스트에서 제일 큰 수를 출력
print(max(result))
