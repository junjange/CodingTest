import sys

t = int(sys.stdin.readline())

# 피보나치 초기 값
fibonacci = [0, 1]

# 피보나치 번호 45, n = 1134903170
for x in range(2, 46):
    fibonacci.append(fibonacci[x-2] + fibonacci[x-1])

# 각 테스트 별로 피보나치 수 출력
for _ in range(t):
    n = int(sys.stdin.readline())
    res = []

    # 제일 큰 수에 피보나치 수부터 반복하여 비교한다.
    for i in range(45, 0, -1):

        # 피보나치 수가 정수보다 작은 경우 res 리스트에 피보나치 수를 추가하고
        # 정수를 피보나치 수만큼 빼준다.
        if fibonacci[i] <= n:
            res.append(fibonacci[i])
            n -= fibonacci[i]

            # 더이상 빼줄 정수가 없는 경우
            if n == 0:
                # res 리스트를 오름차순으로 정렬하여 순서대로 출력한다.
                res.sort()
                for result in res:
                    print(result, end=" ")

                break
