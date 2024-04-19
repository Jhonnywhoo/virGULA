import os
import pwinput
import locale
# Programa para uma empresa de fast food

# Função para carregar dados do TXT
def LoadTxt():
    L0=[] # Lista que recebrá TXT
    L1={} # DCT que receberá a lista
    with open("main.txt",'r') as Dados:
        for i in Dados:
            L0.append(i.strip().split(","))
    for i in L0: # Tranforma lista em dicionario
        L1[i[0]]=[i[1],i[2]]
    return L1

# Função para salvar TXT
def SaveTxt(Dict):
    with open("main.txt", 'w+') as Dados:
        for chave,dados in Dict.items():
            Dados.write(f"{chave},{dados[0]},{dados[1]}\n")

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
    limpar_tela()
    usuario = input('''
BEM VINDO!
Nome: ''')
    Login = LoadTxt() # Carrega os dados dentro da função aut
    for login,valores in Login.items():
        print (f'{login}')
        if usuario == valores[0]:
            print(f'{Login}')
            senha = pwinput.pwinput(prompt='''
ADMINISTRADOR (Digite 99 para sair)
Senha: ''')
            if senha == "99":
                return aut()
            elif senha == valores[1]:
                return adm()
            else:
                while senha not in valores[1]:
                    limpar_tela()
                    senha = pwinput.pwinput(prompt='''
SENHA INCORRETA (digite 99 para sair)
Senha: ''')
                    if senha == "99":
                        return aut()
                    elif senha == valores[1]:
                        limpar_tela()
                        return adm()

    else:
                limpar_tela()
                print(f'Olá, {usuario}!')
                main()

# Função para tela de ADMINISTRADOR
def adm():
    limpar_tela()
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
            limpar_tela()
            mostrar_cardapio()
        elif opcao == "2":
            print()
        elif opcao == "3":
            print()
        elif opcao == "4":
            limpar_tela()
            Login = LoadTxt()
            usuario_teste=input("Digite o usuário administrador atual: ")
            for login,dados in Login.items():
                while usuario_teste not in dados[0]:
                    print("\nUsuário administrador incorreto, tente novamente (digite 99 para cancelar).")
                    usuario_teste=input("\nDigite o usuário administrador atual: ")
                    if usuario_teste == "99":
                        return adm()
                if usuario_teste == dados[0]:
                    usuario_novo = input("Digite o novo usuário administrador: ")
                    L1 = SaveTxt
                    L2 = {
                        login:[usuario_novo,dados[1]]
                    }
                    SaveTxt(L2)
                    input("\nSalvo com sucesso! Pressione enter para continuar")
                    return adm()
                
        elif opcao == "5":
            limpar_tela()
            Login = LoadTxt()
            senha_teste = input("Digite a senha atual: ")
            for login,dados in Login.items():
                while senha_teste not in dados[1]:
                    limpar_tela()
                    print("Senha incorreta, tente novamente. (digite 99 para sair).\n")
                    senha_teste = input("Digite a senha atual: ")
                    if senha_teste == "99":
                        return aut()
                if senha_teste in dados[1]:
                    limpar_tela()
                    nova_senha = input("Digite a nova senha: ")
                    L2 = {
                        "login":[dados[0],nova_senha]
                    }
                    SaveTxt(L2)
                    input("\nSalvo com sucesso! Pressione enter para continuar")
                    return aut()
                
        elif opcao == "6":
            aut()
            return()
        else:
            limpar_tela()
            print("\nOpção inválida, tente novamente.")

# Função para mostrar o cardápio inteiro
def mostrar_cardapio():
    limpar_tela()
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
    limpar_tela()
    mostrar_cardapio()
    escolha = input("Escolha um combo (ex: 1): ")
    if escolha in cardapio:
        return {escolha: cardapio[escolha]}
    else:
        print("Combo não encontrado.")
        return {}

# Função para montar um pedido personalizado
def montar_pedido():
    limpar_tela()
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
    limpar_tela()
    print('Seu carrinho')
    print(carrinho)

#função limpar tela
def limpar_tela():
    #Comando para ver qual sistema operacional está sendo utilizado
    sistema_operacional = os.name
        
    if sistema_operacional == 'posix': #Se for Unix/Linux/MacOS
        os.system('clear')
    elif sistema_operacional == 'nt': #Se for Windows
        os.system('cls')
    
    else: #Caso não seja identificado ele vai executar os dois comandos
        os.system('clear')
        os.system('cls')

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
            limpar_tela()
            mostrar_cardapio()
            
        elif opcao == '2':
            limpar_tela()
            pedido = pedir_combo()
            print("Pedido: ", pedido)

        elif opcao == '3':
            limpar_tela()
            pedido = montar_pedido()
            print("Pedido completo: ", pedido)

        elif opcao == '4':
            ver_carrinho()

        elif opcao == '5':
            limpar_tela()
            print("\nObrigado por usar o programa!\n")
            break
        else:
            limpar_tela()
            print("Opção inválida. Tente novamente.\n")

# Executar o programa
aut()

    