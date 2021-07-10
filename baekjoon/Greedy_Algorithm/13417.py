import sys

t = int(sys.stdin.readline())

for _ in range(t):
    res = []
    n = int(sys.stdin.readline())
    c = sys.stdin.readline().split()

    # 첫 번째 카드는 조건의 상관없이 리스트에 추가한다.
    res.append(c[0])

    # 첫 번째 카드를 제외한 카드부터 마지막 카드까지 비교한다.
    for i in range(1, n):

        # 아스키코드로 비교한다.
        # 첫번째 카드의 아스키코드가 다음 카드의 아스키 코드보다 작으면 제일 뒤에 카드를 추가한다.
        if ord(res[0]) < ord(c[i]):
            res.append(c[i])

        # 반대로 첫번째 카드 아스키코드가 크면 인덱스 기준으로 0번째자리에 다음 카드를 추가한다.
        else:
            res.insert(0, c[i])

    # join 함수를 통해 리스트를 문자열로 바꿔 출력한다.
    print(''.join(res))
