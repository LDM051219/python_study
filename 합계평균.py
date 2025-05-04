numbers = []

while len(numbers) < 5:
        num = int(input(f"{len(numbers) + 1}번째 숫자를 입력하세요 (10보다 큰 양의 정수): "))
        if num > 10:  # 조건: 10보다 큰 양의 정수
            numbers.append(num)  # 조건을 만족하면 리스트에 추가
        else:
            print("10보다 큰 숫자를 입력해주세요.")

# 합계와 평균 계산
total = sum(numbers)
average = total / len(numbers)

# 결과 출력
print(f"입력한 숫자: {numbers}")
print(f"합계: {total}")
print(f"평균: {average:.2f}")
