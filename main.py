import os
import pwinput

# Programa para uma empresa de fast food
itens={
    'Hambúrgueres':{'Cheeseburger': 19.90,'Frango': 14.90,'Duplo Burger': 25.90},
    'Copo':{'Refri 200ml': 4.90,'Refri 600ml': 12.90},
    'Batata':{'Pequena': 5.90, 'média': 8.90, 'grande': 11.90},
    'Sobremesa':{'Milk-shake': 15.90, 'Petit-Gateau': 10.90, 'Casquinha': 5.90}
}

# Dicionário para armazenar os combos/lanches
cardapio = {
    1: {'Carne':' Cheeseburger', 'Acompanhamento':' Batata frita pequena','Copo ':' 200ml','preço': 39.90},
    2: {'Carne':' Frango', 'Acompanhamento':' Batata frita média','Copo':' 200ml','preço': 36.90},
    3: {'Carne':' Duplo Burger', 'Acompanhamento':' Batata frita média','Copo':' 200ml','preço': 49.90},
    4: {'Carne':' Duplo Burger', 'Acompanhamento':' Batata frita grande','Copo':' 600ml','preço': 59.90}
}

# Função de autenticação
def admin():
    while usuario == "admin":
        os.system('clear')
        senha = pwinput.pwinput(prompt='''
ADMINISTRADOR (Digite 99 para sair)
Senha: ''')
        if senha == "99":
            print("Obrigado por usar o programa!\n")
            break
        elif senha == "admin":
            print('''
ADMINISTRADOR''')
            main() ###### TEMPORARIO
        else:
            while senha != "admin":
                os.system('clear')
                flag = True
                senha = pwinput.pwinput(prompt='''
SENHA INCORRETA (digite 99 para sair)
Senha: ''')
                if senha == "99":
                    os.system('clear')
                    print("Obrigado por usar o programa!\n")
                    break
                elif senha == "admin":
                    os.system('clear')
                    print('''
ADMINISTRADOR''')
                    main() ###### TEMPORARIO
        if flag == True:
            break

    else:
        os.system('clear')
        print(f'{usuario},')
        main()

# Função para mostrar o cardápio inteiro
def mostrar_cardapio():
    print('''
        CARDÁPIO
''')
    for combo, itens in cardapio.items():
        print(f"{combo}:")
        for chave, valor in itens.items():
            print(f" {chave}:{valor}")
        print()

# Função para pedir um combo do cardápio
def pedir_combo():
    mostrar_cardapio()
    escolha = input("Escolha um combo (ex: 1): ")
    if escolha in cardapio:
        return {escolha: cardapio[escolha]}
    else:
        print("Combo não encontrado.")
        return {}

# Função para montar um pedido personalizado
def montar_pedido():
    pedido = {}
    print("Monte seu pedido (digite 'sair' para finalizar):")
    while True:
        item = input("Adicione um item ao pedido: ")
        if item == 'sair':
            break
        quantidade = int(input(f"Quantidade de {item}: "))
        pedido[item] = quantidade
    return pedido

# Função principal
def main():
    while True:
        print("digite o número do que gostaria de fazer agora:")
        print("\n1. Mostrar cardápio")
        print("2. Pedir um combo")
        print("3. Montar seu próprio pedido")
        print("4. Ver carrinho")
        print("5. Sair\n")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            os.system('clear')
            mostrar_cardapio()
        elif opcao == '2':
            os.system('clear')
            pedido = pedir_combo()
            print("Pedido: ", pedido)
        elif opcao == '3':
            os.system('clear')
            pedido = montar_pedido()
            print("Pedido completo: ", pedido)
        elif opcao == '5':
            os.system('clear')
            print("\nObrigado por usar o programa!\n")
            break
        else:
            os.system('clear')
            print("Opção inválida. Tente novamente.\n")

# Executar o programa
os.system('clear')
usuario = input('''
BEM VINDO!
Nome: ''')
admin()

    