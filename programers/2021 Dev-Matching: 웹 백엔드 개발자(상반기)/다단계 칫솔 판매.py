def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for _ in range(len(enroll))]))

    # 반복문을 통해 판매원을 확인
    for i in range(len(seller)):
        money = amount[i] * 100 # 판매수량 * 100
        target = seller[i] # 조직 구성원(현재 판매원)

        # 반복문을 통해 판매원의 추천인을 확인
        while True:
            # 현재 판매금액이 10원보다 작다면 현재 조직 구성원에게 돈을 다 주고 반복을 멈춘다.
            if money < 10:
                answer[target] += money
                break

            # 현재 판매금액이 10원보다 크다면
            else:
                # 10%를 제외하고 현재 조직 구서원에게 돈을 준다.
                send = money // 10
                mine = money - send
                answer[target] += mine

                # 현재 조직 구성원이 민호라면 반복을 멈춘다.
                if parent[target] == "-":
                    break
                
                # 현재 조직 구서원이 민호가 아니라면 추천인에게 남은돈을 준다.
                money = send
                target = parent[target]
    
    # list형식으로 answer의 values 값을 출력
    return list(answer.values())

