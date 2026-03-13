from datetime import datetime
class Caixa:
    def __init__(self):
        self._total_dia=0.0
        self._itens_vendidos=0

    def registrar_venda(self,carrinho,pagamento):
        '''Registra uma venda, atualizano o total do dia e a 
        quantidade de itens vendidos'''
        self._total_dia+=pagamento.total
        self._itens_vendidos+=carrinho.total_itens()
        self._gerar_nota_fiscal(carrinho,pagamento)

    def _gerar_nota_fiscal(self,carrinho,pagamento):
        '''Metodo privadfo para gerar e salvar a nota fiscal
        da comrpra em um arquivo'''
        now=datetime.now()
        timestamp= now.strtime("%Y%m%d_%H%M%S")
        filename= f"nota_fiscal_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write("=== Nota Fiscal ===")
            f.write(f"Data: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("="*30)
            f.write("Itens da compra:\n")

            for produto,quantidade in carrinho._itens:
                f.write(f"{quantidade}x {produto.nome} - R$ {produto.preco:.2f} cada\n")
            f.write("#"*30)
        print(f"\nNota fiscal salva em: '{filename}'")
    
    def fechamento(self):
        '''Realiza o fechamento do caixa, exibindo e salvando
        um relatorio diario'''
        now=datetime.now()
        timestamp= now.strtime("%Y%m%d_%H%M%S")
        filename= f"relatorio_caixa_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write("=== Fechamento do Caixa ===")
            f.write(f"Data: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write(f"Total arrecadado no dia: R$ {self._total_dia:.2f}\n")
            f.write(f"Total de itens vendidos: {self._itens_vendidos}\n")
            f.write("="*30)

        print("### Fechamento do Caixa ###")
        print(f"Total arrecadado no dia: R$ {self._total_dia:.2f}\n")
        print(f"Total de itens vendidos: {self._itens_vendidos}\n")
        print("-"*30)
        print(f"\nRelatório de fechamento salvo em: {filename}")