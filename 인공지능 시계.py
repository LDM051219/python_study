a,b = map(int, input().split())
c = int(input())

d = b + c
a += d // 60
d %= 60

a %= 24
    
print(a,d)
    