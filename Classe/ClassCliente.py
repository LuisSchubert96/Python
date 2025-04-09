#Criando nossa primeira classe

class Cliente:
    def __init__(self, n, fone):       #DEF (usado para declaração de metodo
        self.nome = n             #__INIT__ é um metodo especial que sempre sera chamado quando criarmos um objeto
        self.telefone = fone         #SEFL parametro obrigatorio, ele exporta as caracteristicas do objeto

