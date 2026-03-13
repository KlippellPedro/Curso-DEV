import os, json, datetime
from models.produto import Produto
from models.carrinho import Carrinho
from models.pagamento import Pagamento
from models.caixa import Caixa

class Sistema:
    '''Classe que gerencia o fluxo de compra, desde a gestão de produtos
    até o fechamento do caixa'''
    def __init__(self):
        self._arquivo="produto.json"
        self._proximo_codigo=1
        self.produtos: list[Produto]= []
        self.caixa=Caixa()
        self._carregar_produtos()

    def _carregar_produtos(self):
        '''Método protegido para carregar produtos do arquivo JSON.
        Se o arquivo não existir ou for invalido, inicia com uma lista vazia'''
        if os.path.exists(self._arquivo):
            try:
                with open(self._arquivo, "r", encoding="utf-8") as f:
                    dados=json.load(f)
                self.produtos=[Produto.from_dict(d) for d in dados]
                if self.produtos:
                    self._proximo_codigo=max(p.codigo for p in self.produtos)+1
            except Exception as e:
                print(f"Erro ao ler: {self._arquivo}: {e}")
                self._produto= []
                self._proximo_codigo=1
        else:
            self._produto= []
            self._proximo_codigo=1
    
    def menu_gerenciar_produtos(self):
        '''Menu administrativo para gerenciar o estoque'''
        while True:
            print("\n--- Gerenciar Produtos ---")
            print("[1] - Listar produtos")
            print("[2] - Adicionar produto")
            print("[3] - Ajustar estoque de um produto")
            print("[4] - Deletar produto")
            print("[0] - Voltar")
            opc= input("Escolha uma opção: ")

            if opc =="1":
                self.listar_produtos()
            elif opc =="2":
                self.adicionar_produto_interativo()
            elif opc =="3":
                self.ajustar_estoque_interativo()
            elif opc =="4":
                self.deletar_produto_interativo()
            elif opc=="0":
                break
            else:
                print("Opção inválida! Tente novamente.")
    
    def listar_produtos(self):
        '''Mostra todos os produtos disponiveis no terminal'''
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        print("=== \nProdutos ===")
        for p in self.produtos:
            print(p)
    
    def adicionar_produto_interativo(self):
        '''Permite adicionar um novo produto via entrada do usuario'''
        try:
            nome=input("Nome do produto: ")
            preco= float(input("Preço unitário R$ "))
            estoque= int(input("Quantidade inicial no estoque: "))
            novo=Produto(self._proximo_codigo,nome,preco,estoque=estoque)
            self.produtos.append(novo)
            self._proximo_codigo+=1
            self._salvar_produtos()
        except ValueError:
            print("Entrada inválida. Use valores númericos para preço e estoque.")

    
    def ajustar_estoque_interativo(self):
        '''Ajusta o estoque de um produto existente'''
        try:
            codigo= int(input("Informe o codigo do produto: "))
            produto=next((p for p in self.produtos if  p.codigo== codigo),None)
            if produto is None:
                print("Produto não encontrado.")
                return
            novo_estoque=int(input(f"Novo estoque para ´{produto.nome}': "))
            produto.atualizar_estoque(novo_estoque)
            self._salvar_produto()
            print(f"Estoque de '{produto.nome}' atualizado para {produto.estoque}.")
        except ValueError:
            print("Entrada inválida. Use números inteiros para o código e estoque")
    
    def deletar_produto_interativo(self):
        '''Remove permanentemente um produto do catalogo após confirmação'''
        try:
            codigo=int(input("Código do produto a deletar: "))
            produto=next((p for p in self.produtos if codigo == codigo),None)
            if produto is None:
                print("Produto não encontrado.")
                return
            confirma= input(f"Confirma remover '{produto.nome}'? (S/N): ").lower
            if confirma=="s":
                self.produtos.remove(produto)
                self._salvar_produtos()
                print(f"Produto '{produto.nome}' removido do catálogo")
            else:
                print("Operação cancelada.")
        except ValueError:
            print("Entrada inválida.")
    
    # Continuamos na proxima aula 
    