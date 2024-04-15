import os
import pwinput
import locale
# Programa para uma empresa de fast food

# Autenticação de administrador
Login=["admin","1234"]
# Dicionário para armazenar itens e preços individuais
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

carrinho = []

# Função para autenticação
def aut():
    os.system('cls')
    usuario = input('''
BEM VINDO!
Faça o seu login!
Nome: ''')
    while usuario == Login[0]:
        os.system('cls')
        senha = pwinput.pwinput(prompt='''
ADMINISTRADOR (Digite 99 para sair)
Senha: ''')
        if senha == "99":
            return aut()
        elif senha == Login[1]:
            return adm()
        else:
            while senha not in Login[1]:
                os.system('clear')
                senha = pwinput.pwinput(prompt='''
SENHA INCORRETA (digite 99 para sair)
Senha: ''')
                if senha == "99":
                    return aut()
                elif senha == Login[1]:
                    os.system('cls')
                    return adm()

    else:
        os.system('cls')
        print(f'Olá! {usuario}')
        main()

# Função para tela de ADMINISTRADOR
def adm():
    os.system('cls')
    while True:
        print('''
ADMINISTRADOR

1. Mostrar cardápio atual
2. Alterar um combo
3. Alterar preço
4. Alterar usuário administrador
5. Alterar senha administrador
6. Voltar para tela de autenticação (sair)

''')
        opcao=input("ESCOLHA UMA OPÇÃO: ")
        if opcao == "1":
            os.system('cls')
            mostrar_cardapio()
        elif opcao == "2":
            print()
        elif opcao == "3":
            print()
        elif opcao == "4":
            os.system('cls')
            
            usuario_teste=input("Digite o usuário administrador atual: ")
            while usuario_teste not in Login[0]:
                print("\nUsuário administrador incorreto, tente novamente (digite 99 para cancelar).")
                usuario_teste=input("\nDigite o usuário administrador atual: ")
                if usuario_teste == "99":
                    os.system('cls')
                    break
            if usuario_teste == Login[0]:
                usuario_novo = input("Digite o novo usuário administrador: ")
                Login[0] = usuario_novo
                input("\nSalvo com sucesso! Pressione enter para continuar")
                return adm()
                
        elif opcao == "5":
            os.system('cls')
            senha_teste = input("Digite a senha atual: ")
            while senha_teste not in Login[1]:
                os.system('cls')
                print("\nSenha incorreta, tente novamente. (digite 99 para sair).\n")
                senha_teste = input("Digite a senha atual: ")
                if senha_teste == "99":
                    return aut()
            if senha_teste in Login[1]:
                os.system('cls')
                nova_senha = input("Digite a nova senha: ")
                Login[1] = nova_senha
                input("\nSalvo com sucesso! Pressione enter para continuar")
                return aut()
                
        elif opcao == "6":
            aut()
            return()
        else:
            os.system('cls')
            print("\nOpção inválida, tente novamente.")

# Função para mostrar o cardápio inteiro
def mostrar_cardapio():
    print('''
        CARDÁPIO
''')
    for combo, itens in cardapio.items():
        print(f"[{combo}]:")
        for chave, valor in itens.items():
            print(f" {chave}:{valor}")
        print()
    voltarmenu = input("Aperte enter para retornar ao menu: ")

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
    
    for adicional, ingrediente in itens.items():
        print(f"\n{adicional}: \n")
        for chave, valor in ingrediente.items():
            print(f'{chave}: \t R${valor} ')
    while True:
        item = input("Monte o seu proprio pedido: ")
        if item in itens:
            return {item: itens[item]}
        if item == 'sair':
            break
        quantidade = int(input(f"Quantidade de {item}: "))
        carrinho.append({
            "item": item,
            "Quantidade": quantidade
        })
    return carrinho

# Função Ver carrinho
def ver_carrinho():
    os.system('cls')
    print('Seu carrinho')
    print(carrinho)

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
            os.system('cls')
            mostrar_cardapio()
            
        elif opcao == '2':
            os.system('cls')
            pedido = pedir_combo()
            print("Pedido: ", pedido)

        elif opcao == '3':
            os.system('cls')
            pedido = montar_pedido()
            print("Pedido completo: ", pedido)

        elif opcao == '4':
            ver_carrinho()

        elif opcao == '5':
            os.system('cls')
            print("\nObrigado por usar o programa!\n")
            break
        else:
            os.system('cls')
            print("Opção inválida. Tente novamente.\n")

# Executar o programa
aut()

    