import sys

n, k = map(str, sys.stdin.readline().split())
cnt = 0 # 연산 횟수
temp = n # 같은 수를 더하는 연산을 해줄 변수
paper = set() # set() 자료형이 list() 자료형보다 더 빠른 거 같다?..

# 반복문을 통해 n을 몇 번 써야 k로 나누어 떨어지는지 확인
while True:
    temp = int(temp) % int(k) # 나누기 연산
    cnt += 1 # 카운트

    # 나머지가 0이면 나누어 떨이진 것
    if temp == 0:
        break

    else:
        # 같은 수를 더하는 연산
        temp = str(temp) + str(n)

        # 나누어야 하는 수가 집합에 포함되어 있으면
        # 무한 루트이므로 -1 출력
        if temp in paper:
            cnt = -1
            break

        # 나머지 리스트 집합에 나누어야 하는 수를 추가
        paper.add(temp)

print(cnt)
