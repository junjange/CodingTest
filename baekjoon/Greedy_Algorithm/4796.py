import sys
# 첫번째 Case
cnt = 1

while True:

    l, p, v = map(int, sys.stdin.readline().split())

    # 마지막 줄에 0이 3개 주어지기 때문에 while문을 멈춰준다.
    if l == p == v == 0:
        break

    # divmod는 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 반환한 것이다.
    # 따라서 a 는 몫, b 는 나머지
    a, b = divmod(v, p)
    print(a,b)
    # V일짜리 휴가를 캠핑장이 연속하는 P일로 나누게되면 캠핑장을 몇번 갈 수 있는지 나온다.(몫)
    # 나머지가 L일보다 작으면 나머지만큼 또 캠핑장을 갈 수 있고 나머지가 크면 L일만큼 또 갈 수 있다.
    if b <= l:

        print("Case {}: {}".format(cnt, a * l + b))

    else:

        print("Case {}: {}".format(cnt, a * l + l))

    #Case 횟수 카운트
    cnt += 1