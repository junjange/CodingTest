import sys

e, s, m = map(int, sys.stdin.readline().split())
curr_e = 0 # 현재 지구
curr_s = 0 # 현재 태양
curr_m = 0 # 현재 달
cnt = 0 # 우리가 알고 있는 연도

# 반복문을 통해 연도를 계산
while True:
    # 우리가 알고 있는 연도 카운트
    cnt += 1

    # 각 범위에 맞게 지구, 태양, 달을 카운트
    if curr_e == 15:
        curr_e = 1
    else:
        curr_e += 1

    if curr_s == 28:
        curr_s = 1
    else:
        curr_s += 1

    if curr_m == 19:
        curr_m = 1
    else:
        curr_m += 1

    # 구해야하는 지구, 태양, 달의 수라면 
    # 우리가 알고 있는 연도를 출력하고 반복을 멈춘다.
    if curr_e == e and curr_s == s and curr_m == m:
        print(cnt)
        break
