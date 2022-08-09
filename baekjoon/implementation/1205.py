import sys


n, next_point, p = map(int, sys.stdin.readline().split())

# 랭킹 리스트에 점수가 있는지 확인
if n:
    m = sorted(list(map(int, sys.stdin.readline().split())) + [next_point], reverse=True) # 랭킹 리스트 + 새로운 점수
    answer = m.index(next_point) + 1  # 랭킹 리스트에 새로운 점수의 등수

    # 등수가 랭킹의 올라갈 수 있는 둥수보다 크다면 -1 출력
    if answer > p:
        print(-1)
    else:
        # 랭킹 리스트의 길이와 랭킹의 올라갈 수 있는 등수의 길이가 같고 마지막 등수가 새로운 점수의 등수와 같다면
        # 즉, 새로운 점수가 마지막 점수와 동점이라면 -1 출력
        if n == p and next_point == m[-1]:
            print(-1)

        # 위 경우가 아니라면 랭킹 리스트에 새로운 점수의 등수를 출력
        else:
            print(answer)


# 랭킹 리스트에 점수가 없다면 무조건 1등!
else:
    print(1)




