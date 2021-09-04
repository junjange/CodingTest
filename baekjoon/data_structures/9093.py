import sys

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):

    stack = list(map(str, sys.stdin.readline().split()))
    res = ""

    # 리스트를 확인
    for i in stack:
        # 리스트 안에 있는 문자를 거꾸러 출력
        for j in i[::-1]:
            # 거꾸로 된 문자를 더한다.
            res += j
        # 문자열 하나가 끝날 때마다 띄어쓰기
        res += " "
    
    # 문자열 출력
    print(res)
