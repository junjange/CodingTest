n = int(input())
i = []
# 회의시간을 회의 갯수만큼 반복하여 입력받는다.
for _ in range(n):
    i.append(list(map(int,input().split())))

# 회의 시작시간 기준으로 정렬하고 회의 종료시간 기준으로 다시 정렬한다.
i = sorted(i, key=lambda i: i[0])
i = sorted(i, key=lambda i: i[1])
# 비교할 종료시간 초기값
target = 0
# 회의 개수
count = 0
# 시작시간과 종료시간을
for start, end in i:
    # target보다 시작시간이 크거나 같으면 회의를 배정한다.
    if start >= target:
        # 회의 수 카운트
        count += 1
        # 현재 회의의 종료시간을 target에 넣는다.
        target = end

print(count)


