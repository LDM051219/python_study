c = int(input())  # 반복 횟수 또는 초기 카운트값

while True:
    a, b = map(int, input().split())
    
    if a > b:
        print("Yes")
    else:
        print("No")
    
    c -= 1  # 반복 횟수 감소

    if c == 0:  # c가 0이 되면 종료
        print("0 0")
        break
