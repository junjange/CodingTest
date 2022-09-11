def solution(s):
    answer = ''
    nums = s.split(" ")
    nums = list(map(int, nums))
    answer = str(min(nums)) + " " + str(max(nums))
    
    
    return answer
