import sys
sys.setrecursionlimit(10**9)


# 분할 정복
def divide(in_start, in_end, post_start, post_end):

    # 중위 순회 시작점과 끝점이 크로스 되거나 후의 순회 시작점과 끝점이 크로스 되면 리턴
    if(in_start > in_end) or (post_start > post_end):
        return

    # 후위 순회의 끝점이 루트 노드인 것을 이용
    root = postorder[post_end]
    print(root, end=" ") # 각 트리의 루트 노드 출력

    # 중위 순회에서 루트 노드의 좌, 우로 트리가 나뉘는 것을 이용
    left = idx[root] - in_start # 중위 순회 기준으로 왼쪽 인자 갯수
    right = in_end - idx[root] # 중위 순회 기준으로 오른쪽 인자 갯수

    # 왼쪽 서브트리와 오른쪽 서브트리로 나눠 분할 정복을 재귀적으로 수행
    divide(in_start, in_start + left - 1, post_start, post_start + left - 1) # 왼쪽 서브트리
    divide(in_end - right + 1, in_end, post_end - right, post_end - 1) # 오른쪽 서브트리


n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

# 후위 순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인을 위해
# 중위 순회의 값들의 인덱스값을 저장
idx = [0] * (n + 1)
for i in range(n):
    idx[inorder[i]] = i

# 중위 순회, 후위 순회의 성질을 이용하여 분할 정복한다.
divide(0, n - 1, 0, n - 1)
