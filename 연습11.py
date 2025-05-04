a = 4.24E10
print(a)
b = 4.24e10
print(b)
if a == b:
    print("같다")
else:
    print("다르다")

c = 5
d = 3

e = c / d 
e1 = c // d
print("\n%lf"%e)
print(e1)

if(e == e1):
    print("같다")
else:
    print("다르다")

a1 = "python "
a1 = a1 * 20
print("\n%s"%a1)

a2 = "\n%10.4f" % 3.42134234
print(a2)

print("\n{0:=^10}".format("hi"))

dic = {'name':'pey','phone':'010-6409-8953','birth':'1118'}
print(dic)

s1 = set([1,2,3])
print(s1)
s2 = set("Hello")
print(s2)

a,b = ('python','life')
print(b,a)

from copy import copy
a = [1,2,3]
b = copy(a)
print(b is a)

