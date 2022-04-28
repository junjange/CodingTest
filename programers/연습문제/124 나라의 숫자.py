def solution(n):
    answer = ''
    numbers = ['4', '1', '2']
    
    # 3진수로 확인 => 다른점은 3으로 나누어 떨어질 때 n - 1를 해준다.(0이 없기 때문.)
    while n > 0:
        n, mod = divmod(n, 3) # 몫, 나머지
        answer = numbers[mod] + answer 
        
        # 나머지가 0이라면 3으로 나누어 떨어 진 것으로 자릿수 이동 x
        if mod == 0:
            n -= 1
    
    return answer
