import sys
cnt = 1
while 1:

    l,p,v =map(int,sys.stdin.readline().split())

    if l == p ==v==0:
        break
    # divmod는 첫번째 인자를두번째 인자로 나눈 몫과 나버지를 tuple 형식으로 반환한 것이다.
    # 따라서 a 는 몫, b 는 나머지
    a, b =divmod(v,p)
    if b <= l:

        print("Case {}: {}".format(cnt, a * l + b))

    else:

        print("Case {}: {}".format(cnt, a * l + l))
    cnt += 1
