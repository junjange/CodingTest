import sys

while True:
    t = list(map(int, sys.stdin.readline().split()))
    # 입력이 0이면 멈춘다.
    if t == [0]:
        break
    numbers = sorted(t[1:]) # 오름차순으로 정렬
    zeros = numbers.count(0) # 0의 개수
    n, m = '', ''

    # 반복문을 통해 균일하게 수를 배분
    for i in range(zeros, len(numbers)):
        if (zeros - i) % 2 == 0:
            n += str(numbers[i])
        else:
            m += str(numbers[i])
    new_n = n
    new_m = m

    # 반복문을 통해 0을 추가
    for i in range(zeros):
        if len(n) == len(m):
            if i % 2 == 0:
                new_n = new_n[0] + '0' + new_n[1:]
            else:
                new_m = new_m[0] + '0' + new_m[1:]
        else:
            if i % 2 == 0:
                new_m = new_m[0] + '0' + new_m[1:]
            else:
                new_n = new_n[0] + '0' + new_n[1:]

    print(int(new_n) + int(new_m))
