a,b,c = map(int, input().split())
if a == b == c:
    print(10000+a*1000)
elif a == b and a != c and b != c:
    print(1000+a*100)
elif a == c and a != b and c != b:
    print(1000+c*100)
elif b == c and b != a and c != a:
    print(1000+b*100)

else:
    d = [a,b,c]
    d.sort()
    n = d[2]
    print(n*100)
