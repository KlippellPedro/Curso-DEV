from datetime import datetime

class Funcionario:
    def __init__(self,nome,valor_hora,horas,vale_alimentacao,vale_transporte):
        self.nome=nome
        self.valor_hora=float(valor_hora)
        self.horas=float(horas)
        self.vale_alimentacao=float(vale_alimentacao)
        self.vale_transporte=float(vale_transporte)
        
        # Gerar uma matricula automatica usando data e hora atual
        self.matricula=datetime.now().strftime("%Y%m%d%H%M%S")        
        # Calcula o salário bruto
        self.salario_bruto=self.valor_hora*self.horas
        # Calculo do INSS
        self.inss=self.calcular_inss()
        # Calculo do IR
        self.irrf=self.calcular_irrf()
        # Calculo do desconto VA - 6%
        self.desconto_va=self.vale_alimentacao*0.06
        # Calculo do desconto VT - 6% do salário bruto
        self.desconto_vt=self.salario_bruto*0.06
        # Limita o desconto VT ao valor recebido
        if self.desconto_vt> self.vale_transporte:
            self.desconto_vt=self.vale_transporte
        
        # Total de descontos
        self.total_descontos=(self.inss+self.irrf+self.desconto_va+self.desconto_vt)
        # Salário líquido
        self.salario_liquido=self.salario_bruto-self.total_descontos
    
    # Função para o calculo do inss
    def calcular_inss(self):
        salario=self.salario_bruto
        
        faixas=[(1412.00,0.75),(266.68,0.09),(4000.03,0.12),(7786.02,0.14)]
        inss=0
        limite_anterior=0
        
        for limite, aliquota in faixas:
            if salario>limite:
                base=limite-limite_anterior
                inss+=base*aliquota
            else:
                base=salario-limite_anterior
                inss+=base*aliquota
                break
            limite_anterior=limite
        teto=908.85
        if inss>teto:
            return teto
        return round(inss,2)
    
    # Função para o calculo do IRRF
    def calcular_irrf(self):
        base=self.salario_bruto-self.inss
        if base<=2259.20:
            return 0
        elif base<=2826.65:
            return round(base*0.075-169.44,2)
        elif base<=3751.05:
            return round(base*0.15-381.44,2)
        elif base<=4664.68:
            return round(base*0.225-662.44,2)
        else:
            return round(base*0.275-896.00,2)
        