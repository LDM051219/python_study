# read_data_0.py
f = open("C:/tmp/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line.strip())  # 줄바꿈 문자를 없애기 위해 .strip() 사용
f.close()
