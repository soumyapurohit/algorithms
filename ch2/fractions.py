class Fraction:

    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom

    def show(self):
        print(self.num,'/',self.den)
    
    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def __add__(self,other):

        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        common = gcd(newnum,newden)

        return Fraction(newnum//common,newden//common)

    def getNum(self):
        return self.num
        
    def getDen(self):
        return self.den

def gcd(m,n):
    while m%n !=0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n
f1 = Fraction(1,4)
f2 = Fraction(1,2)
#__add__ method is overriden here
f3=f1+f2
print(f3)
f1.show()
f2.show()
print(f1.getNum())
print(f1.getDen())
