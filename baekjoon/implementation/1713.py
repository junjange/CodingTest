import sys
from collections import defaultdict
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
recommend = list(map(int, sys.stdin.readline().split()))
temp = defaultdict(int)

# 반복문을 통해 추천을 확인
for i in range(m):

    # 추천
    temp[recommend[i]] += 1
    # 추천 받은 사람의 수가 사진틀보다 크다면
    # 추천 받은 사람의 사진중에서 하나를 삭제해야한다.
    if len(temp) > n:
        num = float('inf')

        # 반복문을 통해 추천 받은 사람을 확인
        for j in temp:
            # 추천 받은 사람이 현재 추천한 사람의 행위이면 넘긴다. => 무조건! 들어가야 하기 때문
            if j == recommend[i]:
                continue

            # 추천 받은 횟수가 제일 적은 사람을 찾는다.
            if temp[j] < num:
                target = j
                num = temp[j]

        # 추천 받은 홧수가 제일 적은 사람을 삭제
        del temp[target]


# 오름차순으로 출력
answer = []
for k in temp:
    answer.append(k)
print(*sorted(answer))
