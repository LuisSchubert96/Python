
class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone
    # Utilizamos o _ antes do nome para deixarmos apenas as nossas classes e subclasses com acesso ao metodo

    #Metodo GET
    def get_nome(self):
        return self._nome

    def get_telefone(self):
        return self._telefone
    #Metodo Set
    def set_nome(self, nome):
        self._nome = nome
    def set_telefone(self, telefone):
        self._telefone = telefone
