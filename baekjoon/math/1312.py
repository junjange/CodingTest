import sys

a, b, n = map(int, sys.stdin.readline().split())
print(a/b)
a %= b # 처음에 a를 b로 나눠준다. (1의 자리수)
print(a)
# n - 1 반복을 통해 나눗셈을 구현
for _ in range(n - 1):
    a = (a * 10) % b
    print(a)

res = (a * 10) // b # 마지막 나눗셈의 몫을 출력(n의 자리수)
print(res)
