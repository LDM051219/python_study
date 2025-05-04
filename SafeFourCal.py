import FourCal
class SafeFourCal(FourCal.FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
    def mul(self):
        if self.second == 0:
            return 0
        else:
            return self.first * self.second
        
a = SafeFourCal(15,5)

print(a.div())
print(a.mul())