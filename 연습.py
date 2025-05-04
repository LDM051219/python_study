a = int(input())
b = int(input())

c = a*b

print((b % 10) * a)                    #1
print(((b % 100) // 10) * a)           #2
print((b // 100) * a)                  #3
print(c)                               #4