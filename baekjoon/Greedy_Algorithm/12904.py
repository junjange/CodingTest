s = list(input())
t = list(input())
res = 0

# t 리스트를 뒤에서부터 반복하여 확인한다.
for i in range(len(t) - 1, -1, -1):

    # t와 s가 같으면 멈춘다.
    if t == s:
        res = 1
        break

    # t[i]가 A이면 t를 팝해준다.
    if t[i] == "A":
        t.pop()

    # 그 외인 t[i]가 B일 경우 t를 팝하고 거꾸로 바꾼다.
    else:
        t.pop()
        t.reverse()

print(res)

