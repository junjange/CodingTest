def solution(arr):
    answer = 0
    temp = arr.pop()
    size = len(arr)
    n = 1
    while True:
        answer = temp* n
        cnt = 0
        for i in arr:
            if answer % i == 0:
                cnt += 1
            else:
                break
        if cnt == size:
            break
        n += 1
                
    return answer
