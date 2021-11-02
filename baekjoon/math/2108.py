import sys
from collections import Counter
n = int(sys.stdin.readline())
m = [int(sys.stdin.readline()) for _ in range(n)]

# 산술 평균
print(round(sum(m) / n))

# 중앙 값
m.sort()
print(m[n//2])

# 최빈값
cnt = Counter(m).most_common(2) # 가장 개수가 많은 k개의 데이터를 리턴

# 데이터가 2개 이상일 경우
if len(cnt) > 1:
    # 2개의 데이터의 value 값이 같은지 확인
    # 같다면 두 번째 key 값을 출력
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
        
    # 다르다면 첫 번째 key 값을 출력
    else:
        print(cnt[0][0])
        
# 데이터가 하나라면 첫 번째 key 값을 출력
else:
    print(cnt[0][0])

# 범위
print(max(m) - min(m))
