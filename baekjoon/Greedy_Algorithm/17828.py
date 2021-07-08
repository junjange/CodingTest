import sys

n, x = map(int, sys.stdin.readline().split())
result = ""

# x가 n보다 작으면 n만큼 환전할 수 없다.
# x가 n * 26 보다 크면 n개의 화폐로 x의 가치만큼 환전할 수 없다.
if n > x or n * 26 < x:
    print("!")
else:
    # 가치 1 화폐, A를 n개만큼 리스트에 넣는다.
    array = ["A"] * n
    # 환전해야하는 돈에서 1의 가치 n개를 환전했으므로 빼준다.
    x -= n
    # 리스트 수행을 위해 n - 1을 한다.
    i = n - 1

    # x가 0이되면 멈춘다.
    while x > 0:
        # 환전해야하는 돈이 25와 같거나 클경우에 A를 Z로 바꿔준다.
        if x >= 25:
            array[i] = "Z"
            i -= 1
            x -= 25

        # 환전해야하는 돈이 25보다 작을경우에 A를 환전해야하는 가치 + 아스키 코드 문자로 바꿔준다.
        else:
            array[i] = chr(x + 65)
            break

    # 반복문을 통해 리스트에 있는 문자를 더해주어 출력한다.
    for j in range(n):
        result += array[j]

    print(result)
