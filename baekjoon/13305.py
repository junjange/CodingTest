n = int(input())
l = list(map(int, input().split()))
o = list(map(int, input().split()))

# 제일 싼 기름을 파는 도시의 위치
a = 0
# 처음 출발할 때 자동차에는 기름이 없기때문에 처음 도시에서 기름을 넣고 출발한다.
result = o[0] * l[0]

for i in range(1, (n-1)):
    # 도시의 기름값을 비교
    # 이전 도시의 기름값이 더 싸면 이전 도시의 기름을 그 다음 도시까지 갈 수 있을만큼만 산다.
    if o[a] <= o[i]:
        result += o[a] * l[i]
    # 다음 도시의 기름값이 더 싸면 다음 도시의 기름을 그 다음도시까지 갈 수 있을만큼만 산다.
    else:
        result += o[i] * l[i]
        # 비교한 도시중에 제일 싼 기름을 파는 도시의 위치를 바꾼다.
        a = i
        
print(result)
