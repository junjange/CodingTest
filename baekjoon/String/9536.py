import sys


t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복
for _ in range(t):
    sound = list(map(str, sys.stdin.readline().split()))
    
    # 반복문을 통해 동물들의 울음소리를 확인
    while True:
        animal = list(map(str, sys.stdin.readline().split()))
        
        # 동물들의 울음 소리가 아닌 질문이 주어지면 반복을 멈춘다.
        if animal[0] == "what":
            print(" ".join(sound))
            break
        
        # 여우가 아닌 다른 동물들의 울음소리를 제거
        while animal[2] in sound:
            sound.remove(animal[2])


