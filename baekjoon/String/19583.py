import sys

s, e, q = map(str, sys.stdin.readline().split())
dic = {}
answer = {}

while True:
    try:
        time, nick = map(str, sys.stdin.readline().split())

        if time <= s:
            dic[nick] = time

        elif e <= time <= q:
            if nick in dic:
                answer[nick] = 1

    except:
        break
print(len(answer))
