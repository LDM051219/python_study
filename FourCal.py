# FourCal.py
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first // self.second
        return result
    

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(100,10)
print("덧셈:",a.add())
print("뺄셈:",a.sub())
print("곱셈:",a.mul())
print("나누셈:",a.div())
print("제곱:",a.pow())
