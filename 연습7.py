import math
a = int(input())
i = 1
n1 = []
for i in range(1,a+1):
     n1.append(i)
result = math.prod(n1)
print(f"{result}!")