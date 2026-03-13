class Pagamento:
    def __init__(self,total):
        self.total=total
        self._forma_pagamento=""
        self._parcelas=1

    def processar_pagamento(self,opcao):
        '''Aplica o desconto ou acrescimo com base na opção
        de pagamento escolhida'''
        if opcao== 1:
            self.total*=0.90
            self._forma_pagamento= "Dinheiro ou Pix - 10% de desconto"
        elif opcao==2: 
            self.total*=0.95
            self._forma_pagamento= "Cartão de débito - 5% de desconto"
        elif opcao==3: 
            self._forma_pagamento= "Cartão de crédito 30 dias - Mesmo valor"
        elif opcao==4:
            self.total*=1.05
            self._forma_pagamento= "Cartão de crédito 2x - 5% de acréscimo"
            self._parcelas= 2
        elif opcao==5:
            self.total*=1.10
            self._forma_pagamento= "Cartão de crédito 3x - 10% de acréscimo"
            self._parcelas= 3
        elif opcao==6:
            self.total*=1.15
            self._forma_pagamento= "Cartão de crédito 4x - 15% de acréscimo"
            self._parcelas= 4
        else:
            raise ValueError("Opção de pagamento inválida!")
        
    def resumo_pagamento(self):
        '''Retorna uma string formatada com o resumo do pagamento'''
        # Verificar se o pagamento foi parcelado para formatar a saída
        if self._parcelas==1:
            return f"Forma: {self._forma_pagamento}\nTotal: R$ {self.total:.2f}"
        else:
            # Calcular o valor de cada parcela
            valor_parcela=self.total/self._parcelas
            return (f"Formas: {self._forma_pagamento}\nTotal: R$ {self.total:.2f}"
                    f"em {self._parcelas}x de R$ {valor_parcela:.2f}")