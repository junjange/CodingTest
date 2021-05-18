# 입력 값을 '-' 기준으로 나누어준다.
m = input().split('-')

result = []
num = 0
for i in m:
    # 입력 값중에서 '+' 들어간 식은 '+'기준으로 나누어 변수에 넣는다.
    a = i.split('+')

    # '+'식이였던 수를 더해주기 위해.
    for j in a:
        num += int(j)
    # 더한값은 결과 리스트에 추가한다.
    result.append(num)
    # 더한 후 초기화
    num = 0

# 첫 번째값 대입
b = result[0]
# 마지막은 남은 모든 값을 빼기 해준다.
print(result)
for k in range(1,len(result)):
    b -= result[k]

print(b)
