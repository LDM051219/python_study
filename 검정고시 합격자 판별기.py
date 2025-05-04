marks = [60,40,100,97,80,20]       #전과목 평균    #검정고시 합격자 판별기
number = 0
for mark in marks:
    number +=1
if mark < 60: 
    print("%d번 학생은 합격입니다 축하드립니다." %number)
    