class Aumento:
    def __init__(self,categoria,salario):
        self.categoria=categoria
        self.salario=salario
        self.salario_novo=0.0
        self.salario_aumento=0.0

    def calculo_salario_novo(self):
        if self.categoria == "A":
            self.salario_novo= self.salario*0.35
        elif self.categoria == "B":
            self.salario_novo= self.salario*0.30
        elif self.categoria == "C":
            self.salario_novo= self.salario*0.25
        elif self.categoria == "D":
            self.salario_novo= self.salario*0.20
        elif self.categoria == "E":
            self.salario_novo= self.salario*0.15
        return self.salario_novo

    def calculo_aumento(self):
        if self.categoria == "A":
            self.valor_aumento= self.salario-self.salario_novo
        elif self.categoria == "B":
            self.valor_aumento= self.salario-self.salario_novo
        elif self.categoria == "C":
            self.valor_aumento= self.salario-self.salario_novo
        elif self.categoria == "D":
            self.valor_aumento= self.salario-self.salario_novo
        elif self.categoria == "E":
            self.valor_aumento= self.salario-self.salario_novo
        return self.valor_aumento