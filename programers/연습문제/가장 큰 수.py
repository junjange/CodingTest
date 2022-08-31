def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(reverse=True, key=lambda x: x*3)

    return str(int(''.join(answer)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
