class Banco:
    def __init__ (self, nome, endereço, cnpj):
        self.nome = nome 
        self.endereço = endereço
        self.cnpj = cnpj
        self.valor = 0
        self.contas = {}

    def cadastrarClientes(self, id, nome, saldo_inical, senha):
        self.senha = senha
        self.id = id 
        self.nome = nome
        self.saldo_inicial = saldo_inical

        self.contas[self.id] = [self.nome, self.saldo_inicial, self.senha]

    
    def getSaldo(self):
        return self.saldo_inicial
    
    def setSaldo(self, saldo_inical):
        self.saldo_inicial = saldo_inical

    def depositar(self,valor):
        valor = valor

        self.valor[self.contas].append(self.saldo_inicial)
        
    def listar_contas(self):
        for chave, valor in self.contas.items():
            print(f'ID: {chave} - Nome: {valor[0]}')


    def retornar_saldos(self):
        for chave, valor in self.contas.items():
            print(f'ID: {chave} - NOME: {valor[0]} - SALDO: {valor[1]}')

    def sacar(self, id, nome, saldo_inical, senha):
        self.senha = senha
        self.id = id 
        self.nome = nome
        self.saldo_inicial = saldo_inical

        self.contas[self.id] = [self.nome, self.saldo_inicial, self.senha]




        

    

