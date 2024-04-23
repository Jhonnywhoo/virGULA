import os
import pwinput
import locale
# Programa para uma empresa de fast food

# Logo
def Logo():
    print('''
         ,e,        e88~~\  888   | 888        e
Y88b    / "  888-~\d888     888   | 888       d8b
 Y88b  / 888 888   8888 __  888   | 888      /Y88b
  Y88b/  888 888   8888   | 888   | 888     /  Y88b
   Y8/   888 888   Y888   | Y88   | 888    /____Y88b
    Y    888 888    "88__/   "8__/  888___/      Y88b
''')

# Função para carregar dados do TXT
def LoadTxt(tipo='todos'):
    L0=[] # Lista que recebrá TXT
    L1={} # DCT que receberá a lista
    with open("main.txt",'r') as Dados:
        for i in Dados:
            if tipo == 'todos':
                L0.append(i.strip().split(","))
            elif tipo in i:
                L0.append(i.strip().split(","))
    for i in L0: # Tranforma lista em dicionario
        L1[i[0]]=[i[1],i[2]]
    return L1

# Função para salvar TXT
def SaveTxt(Dict):
    with open("main.txt", 'w') as Dados:
        for chave,dados in Dict.items():
            Dados.write(f"{chave},{dados[0]},{dados[1]}\n")

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
    Logo()
    usuario = input('''
BEM VINDO!
Nome: ''')
    if usuario == "fechar":
        return()
    Login = LoadTxt() # Carrega os dados dentro da função aut
    for login,valores in Login.items():
        if usuario == valores[0]:
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
                print(f'\nOlá, {usuario}! Bem vindo ao')
                main()

# Função para alterar usuário
def AltAdm():
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
            while '.' in usuario_novo:
                input("O usuário não pode conter ponto(.), tente novamente: ")
            Login["login"]=[usuario_novo,dados[1]]
            SaveTxt(Login)
            input("\nSalvo com sucesso! Pressione enter para continuar")
            return adm()

# Função para alterar senha de administrador
def AltSenhaAdm():
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
            while '.' in nova_senha:
                nova_senha = input("A senha não pode conter ponto(.), tente novamente: ")
            Login["login"]=[dados[0],nova_senha]
            SaveTxt(Login)
            input("\nSalvo com sucesso! Pressione enter para continuar")
            return adm()

# Função para alterar preço de unidade do montar pedido
def AltUnid():
    limpar_tela()
    print('''
 Aqui é possível alterar o nome e o preço dos itens disponíveis no menu "Montar Combo" dos clientes.
 As alterações são salvas automaticamente no arquivo "main.txt".
''')
    Exib = LoadTxt("[")
    for item,tipo in Exib.items():
        print(item,tipo[0])
        print('R$',tipo[1],'\n')
    Alt = LoadTxt()
    opt = input(('Digite o número do item que gostaria de alterar (digite 99 para sair): '))
    for item,tipo in Exib.items():
        if opt == "99":
            adm()
            return()
        if opt == "1":
            limpar_tela()
            print(f'Lanche:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[1] Lanche:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[1] Lanche:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            else:
                input('\nUnidade não encontrada, pressione Enter para tentar novamente.')
                
        if opt == "2" and item == "[2] Lanche:":
            limpar_tela()
            print(f'Lanche:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[2] Lanche:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[2] Lanche:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
        
        if opt == "3" and item == "[3] Lanche:":
            limpar_tela()
            print(f'Lanche:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[3] Lanche:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[3] Lanche:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
                
        if opt == "4" and item == "[4] Copo de Refrigerante:":
            limpar_tela()
            print(f'Copo de Refrigerante:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[4] Copo de Refrigerante:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[4] Copo de Refrigerante:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
                
        if opt == "5" and item == "[5] Copo de Refrigerante:":
            limpar_tela()
            print(f'Copo de Refrigerante:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[5] Copo de Refrigerante:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[5] Copo de Refrigerante:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
        
        if opt == "6" and item == "[6] Garrafa de Refrigerante:":
            limpar_tela()
            print(f'Garrafa de Refrigerante:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar(Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[6] Garrafa de Refrigerante:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            if alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[6] Garrafa de Refrigerante:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
                
        if opt == "7" and item == "[7] Batata:":
            limpar_tela()
            print(f'Batata:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
               return AltUnid() 
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[7] Batata:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[7] Batata:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
                
        if opt == "8" and item == "[8] Batata:":
            limpar_tela()
            print(f'Batata:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[8] Batata:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[8] Batata:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
                
        if opt == "9" and item == "[9] Batata:":
            limpar_tela()
            print(f'Batata:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[9] Batata:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[9] Batata:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
                
        if opt == "10" and item == "[10] Sobremesa:":
            limpar_tela()
            print(f'Sobremesa:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[10] Sobremesa:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[10] Sobremesa:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
        
        if opt == "11" and item == "[11] Sobremesa:":
            limpar_tela()
            print(f'Sobremesa:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[11] Sobremesa:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[11] Sobremesa:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
        
        if opt == "12" and item == "[12] Sobremesa:":
            limpar_tela()
            print(f'Sobremesa:\n')
            print('[1]',tipo[0])
            print('[2]',tipo[1])
            alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
            if alteracao == "99":
                return AltUnid()
            elif alteracao == "1":
                nome = input("\nDigite o novo nome que gostaria de registrar (Digite 99 para cancelar): ")
                if nome == "99":
                    return AltUnid()
                Alt['[12] Sobremesa:']=[nome,tipo[1]]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
            elif alteracao == "2":
                preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
                if preco == "99":
                    return AltUnid()
                Alt['[12] Sobremesa:']=[tipo[0],preco]
                Alt['[12] Sobremesa:']=[tipo[0],preco]
                SaveTxt(Alt)
                input("\nSalvo!")
                return AltUnid()
                
# Função para tela de ADMINISTRADOR
def adm():
    limpar_tela()
    while True:
        Logo()
        print('''
ADMINISTRADOR

[1] Mostrar cardápio de combos atual

[2] Alterar um combo (cardápio)

[3] Alterar unidade (montar combo)

[4] Alterar usuário administrador

[5] Alterar senha administrador

[6] Voltar para tela de autenticação

[7] Fechar programa

''')
        opcao=input("ENTRE COM O NÚMERO DE UMA DAS OPÇÕES ACIMA: ")
        if opcao == "1":
            limpar_tela()
            mostrar_cardapio()
            return()
        elif opcao == "2":
            print()
        elif opcao == "3":
            AltUnid()
            return()
        elif opcao == "4":
            AltAdm()
            return()
        elif opcao == "5":
            AltSenhaAdm()
            return()
        elif opcao == "6":
            aut()
            return()
        elif opcao == "7":
            limpar_tela()
            print("Obrigado por usar o programa!\n")
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
    Exib = LoadTxt("[")
    for item,tipo in Exib.items():
        print(item,tipo[0])
        print('R$',tipo[1],'\n')
    escolha = input("Digite o iten que você deseja: ")
    print(Exib)

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
        Logo()
        print('''
Sinta-se em casa.
Digite o número do que gostaria de fazer agora:

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

    