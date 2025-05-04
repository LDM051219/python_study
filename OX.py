test = int(input())
while test > 0:
    test -= 1
    a = str(input())
    score = 0 
    current = 0
    for char in a:
        if char == 'O':
            current += 1  
            score += current  
        else:
            current = 0  

    print(score)