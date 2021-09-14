import sys

s = list(map(str, sys.stdin.readline().strip()))
suffix = []

# 문자를 하나씩 제외하여 리스트에 추가
for i in range(len(s)):
    suffix.append(s[i:])

suffix.sort() # 리스트에 있는 문자열을 오름차순으로 정렬

# 정렬된 문자열 리스트를 하나씩 출력
for i in suffix:
    print("".join(i))
