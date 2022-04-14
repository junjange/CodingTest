import sys


# 숫자만 더한다.
def sum_num(num):
    res = 0
    for word in num:
        if word.isdigit():
            res += int(word)
    return res


n = int(sys.stdin.readline())
m = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 정렬(길이, 숫자의 합, 사전순)
m.sort(key=lambda x: (len(x), sum_num(x), x))
for i in m:
    print("".join(i))

