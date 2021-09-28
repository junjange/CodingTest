import sys
import re
from collections import deque

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복하여 문제를 수행
for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    x = str(sys.stdin.readline().strip())
    nums = re.findall("\d+", x) # re 모듈을 통해 문자열 안에 있는 정수만을 추출
    array = deque(nums) # 추출한 정수를 deque에 추가

    rev = False # 거꾸로 뒤집었는지 확인
    error = False # 에러가 생겼는지 확인
    res = [] # 최종 결과

    # 수행해야할 함수를 반복하여 수행
    for i in p:
        # try- except문을 통해 에러를 찾는다.
        try:
            # R 함수이면 거꾸로 뒤집어 준다.
            if i == "R":
                if rev:
                    rev = False
                else:
                    rev = True

            # D 함수이면 rev 변수를 고려하여 앞과 뒤중에 하나를 리스트에서 팝해준다.
            elif i == "D":
                if rev:
                    array.pop()
                else:
                    array.popleft()

        # 에러가 발생하면 error 변수를 True로 바꿔준다.
        except:
            error = True
            break

    # error가 없다면 rev 변수를 고려하여 최종 결과를 출력
    if not error:
        if rev:
            array.reverse()

            res = ",".join(list(array))

        else:
            res = ",".join(list(array))

        print("[" + res + "]")

    # error가 있다면 error를 출력
    else:
        print("error")
