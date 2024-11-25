class c:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1+self.n2
    def kam(self):
        return self.n1-self.n2
class b(c):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def jaran(self):
        return self.n1*self.n2


a=b(4,8)
print(a.kam())
