from Class import *
import os

def main():
    countID = 0
    saldo_inicial = 0
    banco = Banco('Banco Carlinhos', 'Avenida 9 de julho', 12345678)
    Sair = False
    while Sair == False:
        try:
            print('''
    |--------MENU BANCO--------|
    |1- Criar conta            |
    |2- Listar Clientes        |       
    |3- Depositar valor a conta|
    |4- Retornar saldo da conta|    
    |5- Sacar                  |      
    |--------------------------|                
    ''')
            op = int(input('Insira a opção desejada >> '))
            match op:
                case 1:
                    os.system('cls')
                    print('Informe os dados:')
                    nome = input('Insira o seu nome >> ')
                    senha = int(input('Insira sua senha numérica'))
                    countID += 1
                    id = countID
                    saldo_inicial = 0
                    

                    banco.cadastrarClientes(id, nome, saldo_inicial, senha)

                case 2:
                    os.system('cls')
                    banco.listar_contas()
                    os.system('pause')
                
                case 3:
                    os.system('cls')
                    print('Insira o valor que deseja depositar >>')
                    id = int(input('Insira o ID de destino para depósito >> '))
                    nome = input('Insira o nome destino para o depósito >> ')
                    valor = int(input('Insira o valor desejado para o depósito >> '))
                    saldo_inicial += valor
                    banco.cadastrarClientes(id, nome, saldo_inicial, senha)

                    
                    
                case 4:
                    os.system('cls')
                    banco.retornar_saldos()
                    os.system('pause')
                
                case _:
                    print('Opção inválida')

        except ValueError as erro:
            print("Valor Invalido")
            print(f"erro: {erro.__class__.__name__}")                     




