class Produto:
    '''Representa um produto com seu codigo, nome, preço e estoque'''
    def __init__(self,codigo,nome,preco,estoque):
        self._codigo=codigo
        self._nome=nome
        self._preco=preco
        self._estoque=estoque

    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def estoque(self,quantidade):
        '''Setter para o estoque. garante que o estoque não seja negativo'''
        if quantidade>=0:
            self._estoque=quantidade
        else:
            raise ValueError("O estoque não pode ser negativo.")
    
    def reduzir_estoque(self,quantidade):
        '''Reduz o estoque do produto de forma segura'''
        if quantidade<= self._estoque:
            self._estoque-=quantidade
        else:
            raise ValueError("Estoque insuficiente!")
        
    def __str__(self):
        '''Método especial que retorna uma representação em 
        string do objeto'''
        return f"[{self._codigo}] {self._nome} - R$ {self._preco} (Estoque: {self._estoque})"