#Classe Main não possui atributos
class Main:
    pass
print('Testando o código')

#Aqui estamos usando uma linha de código para a importação da classe
#FROM é utilizado para sabermos qual arquivo/módulo sera utilizado
#IMPORT é utilizado para sabermos qual classe iremos importar
from ClassClienteGS import Cliente
from ContaGs import Conta

#Declarando um novo objeto C1
#Passamos para o objeto a Classe que sera instanciada (CLIENTE)
#Passamos os atributos criados no metodo construtor da classe CLIENTE
c1 = ClienteGs('João','519999525225')

#Declarando um novo objeto CONTA
#Passamos para o objeto a Classe que sera instanciada (CONTA)
#Passamos os atributos criados no metodo construtor da classe CONTA
conta = ContaGs(c1.get_nome(),6565,0)

#Primeiro iremos imprimir o a referencia do nosso objeto
print(c1)
#Na sequencia iremos imprimir os dados que armazenamos nela
print(c1.get_nome(),' e ',c1.get_telefone())
#Aqui iremos imprimir os dados armazenados na Classe Conta
print(conta.titular, 'Numero',conta.numero, 'Saldo', conta.saldo)

conta.deposita(200)
conta.saque(50)
conta.extrato()

