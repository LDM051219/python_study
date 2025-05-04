while True:
    try:
        a = int(input("숫자를 입력하세요: "))  # 입력값을 정수로 변환
        if a == 1:
            print("Hello world")
        else:
            print("Good Bye world")

        if a == 0:
            print("출력기를 종료합니다")
            break  # 루프 종료
    except ValueError:
        print("유효한 숫자를 입력하세요.")  # 잘못된 입력 처리
