score = int(input("당신의 점수를 입력해 주세요: "))
score2 = 80 - score

if(score >= 80):
    print("pass")
else:
    print("%d more score"% score2)