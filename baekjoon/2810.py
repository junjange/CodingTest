import sys

n = int(sys.stdin.readline())
seat = input()

# 커플석을 모두 카운트한다.
cnt = seat.count('LL')

# 커플석의 수에 따라 결과가 달라짐
if cnt <= 1:
    # 커플석이 1개보다 작거나 같을 때 모든 사람이 컴홀더를 사용 할 수 있다.
    print(n)

else:
    # 커플석이 2개 이상이면 전체 좌석에서 커플석을 빼고 +1을 해준다.
    print(n - cnt + 1)

