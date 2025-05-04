f = open("C:/tmp/20240853-05.txt", 'w')
coffee = int(input("Coffee count:"))
print(f"Coffee count is {coffee}")
f.write(f"Coffee count is {coffee}\n")

coffee_price = 1000
while True:
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

f.close()
