import sys
import re # 정규 표현식을 지원하는 re 모듈사용

word = str(sys.stdin.readline().rstrip("\n"))
pattern = re.compile('(100+1+|01)+') # re.compile() 함수를 통해 ()안 패턴을 컴파일 한다.
res = pattern.fullmatch(word) # # pattern과 word가 매치되는지 확인

# 매치가 되었다면 잠수함의 엔진소리의 패턴인 것이다.
if res:
    print("SUBMARINE")
else:
    print("NOISE")
