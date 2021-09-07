import sys

n = str(sys.stdin.readline())
res = []
cnt = 0
print(n)
# 입력받은 정수가 두자릿수이면 1의 자리 수의 0을 추가한다.
if len(n) == 2:
    n = "0" + n

while True:
    # 새로운 수를 리스트에 추가한다.
    res.append(n)

    # 두 정수를 더한다.
    temp = int(n[0]) + int(n[1])

    # 두 정수중 오른쪽 자리 수와 더한 수의 오른쪽 자리 수를 붙인다.
    n = n[1] + str(temp)[-1]

    # 리스트에 똑같은 수가 있으면 반복을 멈춘다.
    if n in res:
        break

    # 사이클 횟수 카운트
    cnt += 1

print(cnt)

