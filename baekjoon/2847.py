import sys

n = int(sys.stdin.readline())
point = [int(sys.stdin.readline()) for _ in range(n)]
# 마지막 레벨에서 첫 번째 레벨로 리스트를 거꾸로 바꾼다.
point.reverse()
# 더 높은 레벨의 점수를 타겟으로 정한다.
target = point[0]
res = []
# 마지막 레벨을 제외한 레벨 수만큼 반복한다.
for i in range(1, n):
    # 더 높은 레벨이 그 전 레벨 보다 점수를 더 많이 안주면
    # 더 높은레벨의 점수보다 -1 작게 그 전 레벨의 점수를 받게 한다.
    if target <= point[i]:
        cnt = - (target - point[i] - 1)
        point[i] -= cnt
        res.append(cnt)

    # 타겟을 다음 레벨 점수로 바꾼다.
    target = point[i]

# 리스트에 합을 출력한다.
print(sum(res))
