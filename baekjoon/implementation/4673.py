
# 셀프 넘버가 아닌 수를 찾는 함수
def solution(n):
    n = n + sum(map(int, str(n)))

    return n


answer = []

# 반복문을 통해 셀프 넘버가 아닌 수를 찾는다.
for i in range(1, 10001):
    answer.append(solution(i))

# 반복문을 통해 셀프 넘버가 포함되어 있지 않은 수를 출력
for i in range(1, 10001):
    if i not in answer:
        print(i)
