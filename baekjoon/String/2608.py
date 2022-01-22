import sys


# 아라비아 숫자 구하기
def Arabia(word):
    answer = 0
    visited = [False] * len(word)
    
    # 반복문을 통해 탐색하지 않은 자리수를 확인
    for i in range(len(word)):
        if not visited[i]:
            # 자리수 2개를 합쳤을 때 단어가 two_nums에 있다면 
            if len(word) > i + 1 and word[i: i + 2] in two_nums:
                visited[i: i + 2] = True, True # 탐색 여부
                answer += two_nums[word[i: i + 2]]
                
            # 그 외 단어는 nums에 포함되어 있는 것
            else:
                visited[i] = True  # 탐색 여부
                answer += nums[word[i]]
                
    return answer


# 로마 숫자 구하기
def roma(m):
    answer = ""
    
    # 반복문을 통해 자리수를 확인하면서 로마 숫자로 바꿔준다.
    for i in range(len(m), 0, -1):
        n = int(m[-i]) # 각 자리수의 수 
        
        # 4번째 자리수 
        if i == 4:
            answer += "M" * n
            
        # 3번째 자리수
        elif i == 3:
            if n == 9:
                answer += 'CM'
            elif n == 4:
                answer += 'CD'
            else:
                if n >= 5:
                    answer += 'D'
                answer += 'C' * (n % 5)
        
        # 2번째 자리수
        elif i == 2:
            if n == 9:
                answer += 'XC'
            elif n == 4:
                answer += 'XL'
            else:
                if n >= 5:
                    answer += 'L'
                answer += 'X' * (n % 5)
                
        # 1번째 자리수
        elif i == 1:
            if n == 9:
                answer += 'IX'
            elif n == 4:
                answer += 'IV'
            else:
                if n >= 5:
                    answer += 'V'
                answer += 'I' * (n % 5)
    return answer


nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
two_nums = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

firstWord = str(sys.stdin.readline().rstrip("\n"))
secondWord = str(sys.stdin.readline().rstrip("\n"))
total = Arabia(firstWord) + Arabia(secondWord)
print(total)
print(roma(str(total)))
