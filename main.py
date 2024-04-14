import os
import pwinput

aut_usuario = "admin"
aut_senha = "admin"

# Programa para uma empresa de fast food
itens={
    'Hambúrgueres':{'Cheeseburger': 19.90,'Frango': 14.90,'Duplo Burger': 25.90},
    'Copo':{'Refri 200ml': 4.90,'Refri 600ml': 12.90},
    'Batata':{'Pequena': 5.90, 'média': 8.90, 'grande': 11.90},
    'Sobremesa':{'Milk-shake': 15.90, 'Petit-Gateau': 10.90, 'Casquinha': 5.90}
}

# Dicionário para armazenar os combos/lanches
cardapio = {
    "1": {'Carne':' Cheeseburger', 'Acompanhamento':' Batata frita pequena','Copo ':' 200ml','preço': 39.90},
    "2": {'Carne':' Frango', 'Acompanhamento':' Batata frita média','Copo':' 200ml','preço': 36.90},
    "3": {'Carne':' Duplo Burger', 'Acompanhamento':' Batata frita média','Copo':' 200ml','preço': 49.90},
    "4": {'Carne':' Duplo Burger', 'Acompanhamento':' Batata frita grande','Copo':' 600ml','preço': 59.90}
}

# Função de autenticação
def admin():
    flag = 0
    while usuario == aut_usuario:
        os.system('clear')
        senha = pwinput.pwinput(prompt='''
ADMINISTRADOR (Digite 99 para sair)
Senha: ''')
        if senha == "99":
            print("Obrigado por usar o programa!\n")
            break
        elif senha == aut_senha:
            flag = 1
            print('''
ADMINISTRADOR''')
            adm() ###### TEMPORARIO
        else:
            while senha != aut_senha:
                os.system('clear')
                flag = 1
                senha = pwinput.pwinput(prompt='''
SENHA INCORRETA (digite 99 para sair)
Senha: ''')
                if senha == "99":
                    os.system('clear')
                    print("Obrigado por usar o programa!\n")
                    break
                elif senha == aut_senha:
                    os.system('clear')
                    adm() ###### TEMPORARIO
        if flag == 1:
            break

    else:
        os.system('clear')
        print(f'{usuario},')
        main()

# Função para tela de ADMINISTRADOR
def adm():
    os.system('clear')
    while True:
        print('''
ADMINISTRADOR

1. Mostrar cardápio atual
2. Alterar um combo
3. Alterar preço
4. Alterar usuário ADMINISTRADOR
5. Alterar senha ADMINISTRADOR
6. Sair

''')
        opcao=input("ESCOLHA UMA OPÇÃO: ")
        if opcao == "1":
            os.system('clear')
            mostrar_cardapio()
        elif opcao == "2":
            print()
        elif opcao == "3":
            print()
        elif opcao == "4":
            os.system('clear')
            
            usuario_teste=input("Digite o usuário administrador atual: ")
            while usuario_teste != aut_usuario:
                print("\nUsuário administrador incorreto, tente novamente (digite 99 para cancelar).")
                usuario_teste=input("\nDigite o usuário administrador atual: ")
                if usuario_aut == "99":
                    os.system('clear')
                    break
            if usuario_teste == aut_usuario:
                usuario_novo = input("Digite o novo usuário administrador: ")
                aut_usuario = usuario_novo
                input("\nSalvo com sucesso! Pressione enter para continuar")
                return adm()
                
        elif opcao == "5":
            print()
        elif opcao == "6":
            os.system('clear')
            print("\nObrigado por usar o programa!\n")
            break
        else:
            os.system('clear')
            print("\nOpção inválida, tente novamente.")

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
        print('''
digite o número do que gostaria de fazer agora:

1. Mostrar cardápio
2. Pedir um combo
3. Montar seu próprio pedido
4. Ver carrinho
5. Sair

''')
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

    