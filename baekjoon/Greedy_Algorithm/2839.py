n = int(input())
# 봉지 개수 초기값
result = 0

# 5킬로그램 봉지로 다 가져갈 수 있는지 우선적으로 확인한다.
# 그게 안된다면 3킬로그램 봉지를 하나씩 가져간다.
# 위 두 과정을 반복한다.
while True:
    # 5킬로그램 봉지로 다 가져갈 수 있으면 전체에서 5킬로그램을 나누어 결과값에 넣는다.
    if n % 5 == 0:
        # 결과값과 봉지 개수를 더해서 출력한다.
        result = n // 5 + result
        print(result)
        break
    # 3킬로그램 봉지를 하나 가져간다.
    # 봉지 개수 카운트
    n -= 3
    result += 1

    # 3과 5로 나누어떨어지지 않는다면 -1을 출력한다.
    if n < 0:
        print(-1)
        break