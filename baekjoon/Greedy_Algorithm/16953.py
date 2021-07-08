import sys

a, b = map(int, sys.stdin.readline().split())
# 처음 a 카운트
cnt = 1
# a와 b가 같거나 b로 a를 만들지 못하는 경우를 찾는다.
while True:
    # a와 b가 같으면 멈춘다.
    if a == b:
        break
    # a가 b보다 크면 b로 a를 만들지 못하는 경우임으로 멈춘다.
    elif a > b:
        cnt = -1
        break

    # b가 2로 나눠지면 b를 2로 나눈다.
    if b % 2 == 0:
        b //= 2
    # b를 10으로 나눴을 때 1이 남으면 b를 10으로 나눈 몫으로 바꾼다.
    elif b % 10 == 1:
        b = b // 10

    # 위 두가지 경우가 아니라면 b로 a를 만들지 못하는 경우임으로 멈춘다.
    else:
        cnt = -1
        break

    # 위 두가지 경우이면 카운트한다.
    cnt += 1

print(cnt)



