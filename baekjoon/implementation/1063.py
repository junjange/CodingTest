import sys


k, s, n = map(str, sys.stdin.readline().split())
k = list(map(int, [ord(k[0]) - 64, k[1]]))
s = list(map(int, [ord(s[0]) - 64, s[1]]))
order = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for i in range(int(n)):
    move = str(sys.stdin.readline().strip("\n"))
    kx = k[0] + order[move][0]
    ky = k[1] + order[move][1]

    if 0 < kx <= 8 and 0 < ky <= 8:
        if kx == s[0] and ky == s[1]:
            sx = s[0] + order[move][0]
            sy = s[1] + order[move][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [kx, ky]
                s = [sx, sy]

        else:
            k = [kx, ky]

print(chr(k[0] + 64) + str(k[1]))
print(chr(s[0] + 64) + str(s[1]))
