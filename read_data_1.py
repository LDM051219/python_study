# read_data_1.py
f = open("C:/tmp/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line.strip())  # 줄바꿈 문자를 없애기 위해 .strip() 사용
f.close()