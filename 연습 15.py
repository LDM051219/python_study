N = int(input())

prices =[]
max_price=0

for i in range(N):
    a = int(input())
    b = int(input())
    c = int(input())
    print("")
    if a == b == c:  # 세 숫자가 모두 같은 경우
        price = 10000 + (a * 1000)
        prices.append(price)
    elif a == b or a == c:  # a와 b 또는 a와 c가 같은 경우
        price = 1000 + (a * 100)
        prices.append(price)
    elif b == c:  # b와 c가 같은 경우
        price = 1000 + (b * 100)
        prices.append(price)
    else:  # 모두 다른 경우
        price = max(a, b, c) * 100
        prices.append(price)

max_price = max(prices)


# 리스트 출력
print(max_price)
