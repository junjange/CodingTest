import sys


n, m = map(int, sys.stdin.readline().split())

# 박스가 있다면
if n:
    k = list(map(int, sys.stdin.readline().split()))
    temp = 0 # 가방에 넣을 수 있는 무게
    cnt = 0 # 가방에 넣을 수 있는 책
    
    # 반복문을 통해 책의 무게를 확인
    for i in k:
        temp += i
        
        # 가방에 넣을 수 있는 무게와 가방의 넣을 수 있는 최대 무게가 같을 경우
        if temp == m:
            temp = 0
            cnt += 1
        
        # 가방에 넣을 수 있는 무게가 가방의 넣을 수 있는 최대 무게보다 무거울 경우
        elif temp > m:
            temp = i
            cnt += 1
    
    # 책의 무게를 다 확인 후에도 가방에 넣어야 하는 책이 있는 경우
    if temp:
        cnt += 1

    print(cnt)

# 박스가 없다면
else:
    print(0)
