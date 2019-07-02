
class Power:

    def __init__(self, x, n):

        if x == 1 or n == 0 or n == 1:
            self.x = x
        elif n == 0:
            self.x = 1
        elif x == -1:
            self.x = 1 if n%2 == 0 else -1
        else:
            if n<0:
                x=round(1/x)
                n=abs(n)
                
            if  n<1:
                self.x=pow(x,n)
              
            else:
                self.x=x
                for i in range(1,n):
                    self.x*=x

    def __str__(self):
        return str(self.x)



print(Power(4,0.5))



