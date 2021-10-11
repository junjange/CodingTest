import sys

n = int(sys.stdin.readline())
card = [i for i in range(1, n + 1)]
res = []

while True:
    res.append(card.pop(0)) # 제일 위에 있는 카드를 바닥에 버린다.
    if not card: # 위에서 card 를 팝 했을 때 남은 card 가 없으면 멈춘다.
        break     
    card.append(card.pop(0)) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

print(*res)
