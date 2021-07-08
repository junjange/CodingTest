n = int(input())
p = list(map(int, input().split()))
# 돈을 인출하는데 걸리는 시간을 오름차순으로 정렬한다.
p.sort()
# 기다리는 시간
total = 0
# 총 걸리는 시간
result = 0

for i in p:
    # 돈을 인출하는 시간과 기다리는 시간을 더해준다.
    total = i + total
    # 기다리는 시간을 총 걸리는 시간에 더해준다.
    result += total

print(result)
