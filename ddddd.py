i = int(input())
while i > 0: 
    def gcd(a,b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)
    
    num1,num2 = map(int, input().split())
    result = lcm(num1,num2)
    print(result)
    i-= 1
