import sys
from collections import Counter # collections 모듈에 Counter 클래스 사용

n = int(sys.stdin.readline())
n_card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_card = list(map(int, sys.stdin.readline().split()))

# 숫자 카드에 적혀있는 정수의 개수를 세어준다.
cnt = Counter(n_card)

# 결과 리스트
res = [0] * m

# 구해야 할 정수가 있는지 반복문을 통해 확인한다.
for i in range(m):
    
    # 구해야 할 정수가 있다면 정수의 개수를 구해야 할 카드 자리에 넣어준다.
    if cnt[m_card[i]]:
        res[i] = cnt[m_card[i]]

print(*res)
