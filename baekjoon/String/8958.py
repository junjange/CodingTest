import sys


n = int(sys.stdin.readline())

# 반복문을 통해 테스트 케이스를 실행
for _ in range(n):
    m = list(map(str, sys.stdin.readline().strip()))
    res = 0 # 점수
    cnt = 1 
    
    # 반복문을 통해 문자열을 확인
    for i in m:
        
        # 문자가 'O' 라면 점수에 cnt 를 더하고 cnt 는 +1 해준다.
        if i == "O":
            res += cnt
            cnt += 1 
            
        # 문자가 'X' 라면 점수를 더하지 않고 cnt 를 1로 초기화 해준다.
        else:
            cnt = 1

    print(res) # 점수 출력
