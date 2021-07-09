import sys

n = int(sys.stdin.readline())
# 유제품의 가격을 오름차순으로 정렬하여 입력 받는다.
c = sorted([int(sys.stdin.readline()) for _ in range(n)])
temp = []
res = 0

# 모든 유제품의 가격을 확인할 때까지 반복하여 최소비용을 구한다.
while c:
    # 제일 비싼 유제품을 팝하여 리스트에 넣는다.
    temp.append(c.pop())

    # 비싼 유제품이 들어간 리스트의 길이가 3이 되면
    # 하나를 팝하고 나머지를 더해줘 결과 값에 넣는다.
    # 그리고 다시 제일 비싼 유제품 리스트를 비워준다.
    if len(temp) == 3:
        temp.pop()
        res += sum(temp)
        temp = []

# 나머지 유제품을 구매하고 비용을 출력한다.
res += sum(temp)
print(res)

