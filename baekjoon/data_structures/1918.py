import sys

s = list(map(str, sys.stdin.readline().strip()))
stack = []
res = ""

# 입력받은 문자를 반복문을 통해 확인
for i in s:
    # 피연산자인지 확인
    if i.isalpha():
        res += i
    
    elif i == '(':
        stack.append(i)
        
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1]=='/'):
            res += stack.pop()
        stack.append(i)
        
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(i)
        
    elif i == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()
        
# 스택안에 남아있는 값을 pop
while stack:
    res += stack.pop()
    
print(res)
