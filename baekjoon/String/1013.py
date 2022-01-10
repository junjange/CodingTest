import sys
import re # 정규 표현식을 지원하는 re 모듈

n = int(sys.stdin.readline())

# 반복문을 통해 테스트 케이스를 확인
for _ in range(n):
    t = str(sys.stdin.readline().rstrip("\n"))
    pattern = re.compile('(100+1+|01)+') # re.compile() 함수를 통해 ()안 패턴을 컴파일 한다.
    res = pattern.fullmatch(t) # pattern과 t가 매치되는지 확인

    # 매치가 되면 테스트 케이스는 제시한 패턴인 것이다.
    if res:
        print('YES')
    else:
        print('NO')
