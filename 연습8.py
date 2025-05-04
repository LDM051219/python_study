h = int(input("키를 입력하시오: "))
w = int(input("몸무게를 입력하시오: "))
b = (10000*w) / (h*h)

if(b >= 25):
    print('%d' %b)
    print("Obesity")
else:
    print('%d' %b)
