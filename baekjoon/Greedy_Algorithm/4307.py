import sys


t = int(sys.stdin.readline())

for _ in range(t):
    l, n = map(int, sys.stdin.readline().split())
    ant = [int(sys.stdin.readline()) for _ in range(n)]
    f_ant = 0
    l_ant = 0

    # 모든 개미를 확인
    for i in ant:
        # 개미의 위치가 막대의 우측에 있다면
        if i > l - i:
            # 가장 빠른 시간에 떨어질 경우
            if f_ant < l - i:
                f_ant = l - i
            
            # 가장 늦은 시간에 떨어질 경우
            if l_ant < i:
                l_ant = i
        
        # 개미의 위치가 막대의 좌측에 있다면
        else:
            if f_ant < i:
                f_ant = i

            if l_ant < l - i:
                l_ant = l - i

    print(f_ant, l_ant)
