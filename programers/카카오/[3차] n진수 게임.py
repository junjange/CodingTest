def solution(n, t, m, p):
    answer = '0'
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    # 반복문을 통해 미리 구할 숫자의 갯수를 구하기 위한 게임의
    for i in range(1, t * m):
        temp = []

        # i를 n진수로 변환
        while i > 0:
            i, mod = divmod(i, n)
            temp.append(data[mod]) # 변환한 수를 data에서 뽑아 temp에 추가

        # reversed를 통해 변환한 진수를 answer에 더한다.
        answer += "".join(reversed(temp))
    
    # 0을 포함해야하기 때문에 p-1부터 t*m까지 m번씩 나눈 수를 리턴
    return answer[p-1: t * m: m]

# print(solution(16,16,2,1)) # 예시 코드
