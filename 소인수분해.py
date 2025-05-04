n = int(input("정수를 입력하세요: "))
i = 2  # 소수는 2부터 시작

while n > 1:  # n이 1이 될 때까지 반복
    if n % i == 0:  # n이 i로 나누어떨어지면
        print(i)  # i는 소인수
        n = n // i  # n을 i로 나눔
    else:
        i += 1  # i를 1 증가시켜 다음 숫자로 진행
