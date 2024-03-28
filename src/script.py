import csv
import os

def adicionar_cliente(nome, email, telefone):
    with open('clientes.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, email, telefone])
    print("Cliente adicionado com sucesso!")

def visualizar_clientes():
    with open('clientes.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        for linha in leitor:
            print("Nome: {}, Email: {}, Telefone: {}".format(linha[0], linha[1], linha[2]))

def buscar_cliente(nome):
    with open('clientes.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        encontrado = False
        for linha in leitor:
            if linha[0].lower() == nome.lower():
                print("Cliente encontrado - Nome: {}, Email: {}, Telefone: {}".format(linha[0], linha[1], linha[2]))
                encontrado = True
                break
        if not encontrado:
            print("Cliente não encontrado.")

def main():
    if os.path.exists('clientes.csv'):
        print("O arquivo clientes.csv já existe.")
    else:
        print("O arquivo clientes.csv não existe. Criando arquivo...")
        with open('clientes.csv', 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Nome", "Email", "Telefone"])
        print("Arquivo clientes.csv criado com sucesso!")

    while True:
        print("\nx--------------------------x")
        print("|1. Adicionar Cliente      |")
        print("|2. Visualizar Clientes    |")
        print("|3. Buscar Cliente         |")
        print("|4. Encerrar Programa      |")
        print("x--------------------------x")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            adicionar_cliente(nome, email, telefone)
        elif escolha == '2':
            print("\nLista de Clientes:")
            visualizar_clientes()
        elif escolha == '3':
            nome = input("\nDigite o nome do cliente que deseja buscar: ")
            buscar_cliente(nome)
        elif escolha == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()