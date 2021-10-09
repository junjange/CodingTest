import sys
from collections import Counter

n = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(n)]
card.sort() # 입력받은 숫자 카드를 오름차순으로 정렬
res = Counter(card) # 카드의 개수를 확인
target = [0, 0] # 비교할 타겟 [개수, 정수]

# 반복문을 통해 카드를 확인
for i in res:
    # 타겟의 개수와 현재 카드의 개수를 비교
    if target[0] < res[i]:
        target[0] = res[i] # 타겟의 개수를 현재 카드의 개수로 초기화
        target[1] = i # 타겟의 정수도 현재 카드의 정수로 초기화

# 타겟의 정수 출력
print(target[1])
