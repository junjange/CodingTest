def solution(n, arr1, arr2):
    answer = []

    temp1 = [format(i, 'b').zfill(n) for i in arr1] # arr1 => 2진수 n자리로 변환
    temp2 = [format(j, 'b').zfill(n) for j in arr2] # arr2 => 2진수 n자리로 변환

    # 반복문을 통헤 지도의 각 자리를 비교
    for a1, a2 in zip(temp1, temp2):
        cnt = ""
        for k in range(n):
            # 각 자리의 수를 더했을 때 0보다 크면 : 벽
            if int(a1[k]) + int(a2[k]) > 0:
                cnt += "#"
            # 0보다 작으면 : 공백
            else:
                cnt += " "

        answer.append(cnt)

    return answer


# print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])) # 예시 코드
