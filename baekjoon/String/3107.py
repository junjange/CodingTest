import sys

IPv6 = list(map(str, sys.stdin.readline().strip("\n").split(":")))
idx = []

# 반복문을 통해 각 그룹을 확인
for i in range(len(IPv6)):

    # 0으로만 이루어진 그룹의 idx 저장
    if len(IPv6[i]) == 0:
        idx.append(i)
        continue

    # 0으로 이루어지지 않은 그룹의 0을 추가
    if len(IPv6[i]) < 4:
        IPv6[i] = "0" * (4 - len(IPv6[i])) + IPv6[i]

# 0으로만 이루어진 그룹이 있다면
if idx:

    # 반복문을 통해 IPv6 공백을 제거 
    for _ in idx:
        del IPv6[idx[0]]

    # IPv6의 길이가 8이 될 때까지 0으로만 이루어진 그룹에 "0000"을 추가
    while len(IPv6) != 8:
        IPv6.insert(idx[0], "0000")


print(":".join(IPv6))
