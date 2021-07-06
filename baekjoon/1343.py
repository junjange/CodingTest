dic = input()

# replace 함수를 통해 찾을 값과 바꿀 값을 설정하여 바꿔준다.
dic = dic.replace("XXXX", "AAAA")
dic = dic.replace("XX", "BB")

# 사전에 아직 X가 있으면 -1 출력
if "X" in dic:
    print(-1)
else:
    print(dic)
