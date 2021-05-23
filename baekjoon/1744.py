import sys
n = int(sys.stdin.readline())
# 양수 리스트
po = []
# 음수, 0 리스트
ne = []
# 1 리스트
one = []
# 수열의 합 초기값
result = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    # 수열의 수가 1보다 크면 양수 리스트의 추가
    if num > 1:
        po.append(num)
    # 수열의 수가 0보다 작거나 같으면 음수, 0 리스트의 추가
    elif num <= 0:
        ne.append(num)
    # 수열의 수 1을 1 리스트의 추가
    else:
        one.append(num)
# 양수 리스트를 내림차순으로 정렬
po.sort(reverse=True)
# 음수, 0 리스트를 오름차순으로 정렬
ne.sort()

# 1은 곱하게 되면 그냥 그대로 이기때문에 묶지 않고 결과값과 바로 더해준다.
result += sum(one)

# 양수 리스트를 묶어서 결과값에 더해준다.
if len(po) % 2 == 0:
    for i in range(0, len(po), 2):
        result += po[i] * po[i+1]
else:
    for i in range(0, len(po)-1, 2):
        result += po[i] * po[i+1]
    result += po[-1]

# 음수 리스트를 묶어서 결과값에 더해준다.
# 음수를 묶으면 양수가 된다.
if len(ne) % 2 == 0:
    for i in range(0, len(ne), 2):
        result += ne[i] * ne[i+1]
else:
    for i in range(0, len(ne)-1, 2):
        result += ne[i] * ne[i+1]
    result += ne[-1]


print(result)
