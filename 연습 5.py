score1 = 100
score2 = 100
round1 = int(input("round:"))
while round1 >= 1:
    cube1 = int(input("주사위 값: "))
    cube2 = int(input("주사위 값: "))
    print("")
    if cube1 > cube2:
        score2 = score2 - cube1
        round1 = round1 - 1
        
    if cube1 < cube2:
        score1 = score1 - cube2
        round1 = round1 - 1
    
    if cube1 == cube2:
        round1 = round1 - 1

print(score1)
print(score2)