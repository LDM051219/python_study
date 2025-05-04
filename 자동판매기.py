try:
    f = open("C:/tmp/20240853-05.txt", 'w')
    coffee = int(input("Coffee count:"))
    print(f"Coffee count is {coffee}")
    f.write(f"Coffee count is {coffee}\n")
    coffee_price = 1000

    while True:
        if(coffee <= 0):
            print("커피의 수량을 제대로 입력해주세요")
            f.write("커피의 수량을 제대로 입력해주세요\n")
            break
        money = int(input("Insert money:"))
        print(f"{money} won received.")
        f.write(f"{money} won received.\n")
    
        if money > coffee_price:    
            change = money - coffee_price
            print("커피를 제공합니다")
            f.write("커피를 제공합니다\n")
            print(f"Change is {change} won.")
            f.write(f"Change is {change} won.\n")
            coffee -= 1
        elif money == coffee_price:
            print("커피를 제공합니다.")
            f.write("커피를 제공합니다.\n")
            coffee -= 1
        elif money < coffee_price:
            print("돈이 부족합니다.")
            f.write("돈이 부족합니다.\n")
        
        if coffee == 0:    
            print("Sold out.")
            f.write("Sold out.\n")
            break

except(ValueError):
    print("숫자를 입력하지 않았습니다")
    f.write("숫자를 입력하지 않았습니다\n")

finally:
    print("프로그램이 종료되었습니다")
    f.write("프로그램이 종료되었습니다")

    
    
    f.close()