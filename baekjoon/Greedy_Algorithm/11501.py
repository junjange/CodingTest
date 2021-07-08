import sys

case = int(sys.stdin.readline())

# 케이스만큼 반복한다.
for _ in range(case):
    # 날
    day = int(sys.stdin.readline())
    # 주식의 거래가
    deal = list(map(int, sys.stdin.readline().split()))
    # 총 수익
    stock_return = 0

    # 모든 날을 확인한다.
    while True:

        # 주식이 없으면 반복문을 멈춘다.
        if len(deal) == 0:
            break
        # 마지막 날 주식의 거래가를 팝하여 전날의 모든 주식 거래가를 비교한다.
        sell = deal.pop()

        # 반복문을 통해 주식의 거래가를 마지막 날에 전날에 주식의 판매가부터 첫 날 주식의 가격까지 거꾸로 확인한다.
        for i in reversed(range(len(deal))):
            # 마지막 주식의 판매가가 전날에 판매가보다 크거나 같을 때
            if sell >= deal[i]:

                # 마지막 날에 주식의 거래가에서 그 전날에 주식의 거래가를 빼줘 수익 실현을 한다.
                stock_return += (sell - deal[i])
                # 주식을 팔았으므로 팝한다.
                deal.pop()

            # 마지막 날에 거래가가 그 전날에 거래가보다 작으면 반복을 멈춘다.
            else:
                break

    print(stock_return)
