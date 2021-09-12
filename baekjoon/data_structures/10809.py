import sys

s = list(map(str, sys.stdin.readline().strip()))
res = []
for i in range(26):

    # s 안에 다음 아스키 코드 문자가 있으면
    if chr(97 + i) in s:
        # 아스키 코드가 있는 문자의 인덱스 위치를 res 에 추가.
        res.append(s.index(chr(97 + i)))
    else:
        # 아스키 코드가 없다면 res 에 -1 추가
        res.append(-1)

print(*res)
