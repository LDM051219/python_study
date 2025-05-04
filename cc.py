import random

f = open("C:/tmp/cc.txt", 'w')
computer_num = random.randrange(1, 101)

print("Computer selected a random number.")
f.write("Computer selected a random number.\n")

i = 0
while True:
    i += 1

    my_num = int(input("Input your number (1~100): "))
    f.write(f"Input your number (1~100): {my_num}\n") 

    if computer_num > my_num:
        print("BIG")
        f.write("BIG\n")
    elif computer_num < my_num:
        print("SMALL")
        f.write("SMALL\n")
    elif computer_num == my_num:
        print(f"Bingo! You tried {i} times.")
        f.write(f"Bingo! You tried {i} times.\n")
        break

f.close()
