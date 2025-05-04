n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

cnt = a.count(1)
cnb = a.count(0)
if cnt > cnb:
    print("Junhee is cute!")
else: 
    print("Junhee is not cute!")