class Media:
    def __init__(self,n1,n2,n3,n4,n5):
        self.n1=n1
        self.n2=n2
        self.n3=n3
        self.n4=n4
        self.n5=n5

    def calcular_media(self):
        self.media= (self.n1+self.n2+self.n3+self.n4+self.n5)/5
        return self.media