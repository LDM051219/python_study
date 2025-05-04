class FourCal:
    def setdata(self, first, second):
        self.first = first      #a(self 값)안에다가 무언가를 저장하기 위해서 필요
        self.second = second   
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        result = self.first / self.second  #float
        return result
    def div2(self):
        result = self.first // self.second
        return result
a = FourCal() # a는 계산기 자체를 의미



