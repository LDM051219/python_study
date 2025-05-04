hour,minute,sec = map(int, input().split())
c_t = int(input())

sec2= sec + c_t
sec = sec2 % 60
minute += sec2 // 60
hour = hour + minute // 60
minute %= 60
hour %= 24


print(hour,minute,sec)