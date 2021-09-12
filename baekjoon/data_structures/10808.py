import sys
from collections import Counter # collections 모듈에 Counter 클래스 사용

s = list(map(str,sys.stdin.readline().strip()))
c = Counter(s) # 알파벳 개수를 확인
res = []

# 알파벳 개수만큼 반복
for i in range(26):
    # 리스트에 아스키 코드로 바꾼 값의 알파벳 개수를 추가
    res.append(c[chr(97 + i)])

print(*res)
