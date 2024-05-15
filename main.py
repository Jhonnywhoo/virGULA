'''
Trabalho MINI-CRUD a pedido do Professor Luiz.

Nosso CRUD propõe criar uma ferramenta de gestão e atendimento para um restaurante fast-food baseado em cardápio de combos.
O cardápio principal utiliza funções de dicionário Python, enquanto os itens vendidos separadamente e o login administrativo funcionam em arquivo ".txt".

Jhonny Wendel Oliveira de Brito - 1D ADS
Gustavo de Freitas Andrade - 1D ADS
Enzo Reis Bernardino - 1D ADS
Alex Michel Facciolla da Silva - 1D ADS
'''

import os
import pwinput
import locale
import random
import string
from tabulate import tabulate
from colorama import Fore, Style

# Programa para uma empresa de fast food
carrinho = []

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

# Função principal de atendimento
def main():
    while True:
        Logo()
        print('''
--------------------Sinta-se em casa.-------------------


 -------------------------------------------------------
| Opção |                 Opções                       |
    ----------------------------------------------------
|   1   |          Mostrar cardápio                    |
|   2   |          Pedir um combo                      |
|   3   |          Escolher apenas 1 item              |
|   4   |          Ver carrinho                        |
|   5   |          Finalizar pedido                    |
|   6   |          Sair                                |
--------------------------------------------------------

''')
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            limpar_tela()
            mostrar_cardapio()

        elif opcao == '2':
            limpar_tela()
            pedir_combo()

        elif opcao == '3':
            limpar_tela()
            Pedir_itens()

        elif opcao == '4':
            ver_carrinho()

        elif opcao == '5':
            limpar_tela()
            exibir_carrinho()
            finalizar_pedido()
            classificar_atendimento()
            print("Agradecemos por utilizar o nosso serviço, volte sempre!!!")
            break

        elif opcao == '6':
            limpar_tela()
            print("\nObrigado por usar o programa!\n")
            break
        else:
            limpar_tela()
            print("Opção inválida. Tente novamente.\n")


# Função para tela de ADMINISTRADOR
def adm():
    limpar_tela()
    while True:
        Logo()
        print('''
-------------------------------------------------------
|                 PAINEL DE ADMINISTRAÇÃO             |
-------------------------------------------------------
| Opção |                  Descrição                  |
-------------------------------------------------------
|   1   |    Mostrar cardápio atual                   |
|   2   |    Mostrar itens do menu atual              |
|   3   |    Alterar um item do menu                  |
|   4   |    Adicionar combo                          |
|   5   |    Alterar combo                            |
|   6   |    Remover combo existente                  |
|   7   |    Alterar Usuário administrador            |
|   8   |    Alterar Senha de administrador           |
|   9   |    Sair                                     |
-------------------------------------------------------
\n
''')
        opcao=input("ENTRE COM O NÚMERO DE UMA DAS OPÇÕES ACIMA: ")
        if opcao == "1":
            mostrar_cardapio()
            input("")
            adm()
            return()
        elif opcao == "2":
            exibir_itens()
            return()
        elif opcao == "3":
            AltUnid()
            return()
        elif opcao == "4":
            adicionar_ao_cardapio()
            return()
        elif opcao == "5":
            alterar_do_Cardapio()
            return()
        elif opcao == "6":
            remover_Combo_cardapio()
            return()
        elif opcao == "7":
            AltAdm()
            return()
        elif opcao == "8":
            AltSenhaAdm()
            return()
        elif opcao == "9":
            aut()
            return()
        else:
            limpar_tela()
            input("\nOpção inválida, tente novamente.")

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
            while '.' in usuario_novo: # para evitar conflitos no .txt
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
            while '.' in nova_senha: # Para evitar conflitos no .txt
                nova_senha = input("A senha não pode conter ponto(.), tente novamente: ")
            Login["login"]=[dados[0],nova_senha]
            SaveTxt(Login)
            input("\nSalvo com sucesso! Pressione enter para continuar")
            return adm()

# Funções para alterar preço de unidade do montar pedido
def alterar_item(item, Alt):
    limpar_tela()
    print(f'{item}:\n')
    print('[1]', Alt[item][0])
    print('[2]', Alt[item][1])
    alteracao = input('\nDigite o número do que gostaria de alterar (Digite 99 para cancelar): ')
    if alteracao == "99":
        return
    elif alteracao == "1":
        nome = input(f"\nDigite o novo nome que gostaria de registrar para {item} (Digite 99 para cancelar): ")
        if nome == "99":
            return AltUnid()
        Alt[item][0] = nome
    elif alteracao == "2":
        preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e ponto)
Digite 99 para cancelar: ''')
        if preco == "99":
            return AltUnid()
        Alt[item][1] = preco
    SaveTxt(Alt)
    input("\nSalvo!")
    return AltUnid()

def AltUnid():
    limpar_tela()
    print('''
Aqui é possível alterar o nome e o preço dos itens disponíveis no menu "Escolher apenas 1 item" dos clientes.
As alterações são salvas automaticamente no arquivo "main.txt".
''')
    Exib = LoadTxt("[") # formata uma variável que receba os itens do .txt filtrados, apenas para exibir
    for item, tipo in Exib.items():
        print(item, tipo[0])
        print('R$', tipo[1], '\n')

    Alt = LoadTxt()
    opt = input('Digite o número do item que gostaria de alterar (digite 99 para sair): ')
    if opt == "99":
        return ()
    elif opt.isdigit() and int(opt) <= len(Exib): # filtro para a escolha ser dígito e estar na length no cardápio
        alterar_item(list(Exib.keys())[int(opt) - 1], Alt) # carrega a outra função já com parmetros de lista, excluir primeira linha e variável Alt
    else:
        input('\nOpção inválida, pressione Enter para tentar novamente.')

#Carregar_cardapio
def carregar_cardapio():
    cardapio = {}
    with open("cardapio.txt", "r") as file:
        for line in file:
            id, nome, lanche, acompanhamento, copo, preco = line.strip().split(",")
            cardapio[id] = {'Nome': nome, 'Lanche': lanche, 'Acompanhamento': acompanhamento, 'Copo': copo, 'Preço': float(preco)}
    return cardapio
    

#Mostrar cardapio
def mostrar_cardapio():
    cardapio = carregar_cardapio()
    print(Fore.YELLOW + "CARDÁPIO\n" + Style.RESET_ALL)
    headers = [Fore.GREEN + "ID", "Nome", "Lanche", "Acompanhamento", "Copo", "Preço" + Style.RESET_ALL]
    table_data = []
    for num, combo in cardapio.items():
        row = [num, combo['Nome'], combo['Lanche'], combo['Acompanhamento'], combo['Copo'], f"R${combo['Preço']:.2f}"]
        table_data.append(row)
    print(tabulate(table_data, headers=headers, tablefmt="psql"))

#Adicionar item ao cardapio
def adicionar_ao_cardapio():
    nome = input("Digite o nome do novo item: ")
    lanche = input("Digite o nome do lanche: ")
    acompanhamento = input("Digite o nome do acompanhamento: ")
    copo = input("Digite o tamanho do copo: ")
    preco = float(input("Digite o preço do item: "))
    with open("cardapio.txt", "a") as file:
        id = str(len(carregar_cardapio()) + 1)
        file.write(f"{id},{nome},{lanche},{acompanhamento},{copo},{preco}\n")
    print("Item adicionado ao cardápio!")
    return adm()

#Alterar combo do cardapio 
def alterar_do_Cardapio():
    mostrar_cardapio()
    id = input("Digite o ID do item que deseja alterar: ")
    if id in carregar_cardapio():
        nome = input("Digite o novo nome do item: ")
        lanche = input("Digite o novo nome do lanche: ")
        acompanhamento = input("Digite o novo nome do acompanhamento: ")
        copo = input("Digite o novo tamanho do copo: ")
        preco = float(input("Digite o novo preço do item: "))
        cardapio = carregar_cardapio()
        cardapio[id] = {'Nome': nome, 'Lanche': lanche, 'Acompanhamento': acompanhamento, 'Copo': copo, 'Preço': preco}
        with open("cardapio.txt", "w") as file:
            for id, combo in cardapio.items():
                file.write(f"{id},{combo['Nome']},{combo['Lanche']},{combo['Acompanhamento']},{combo['Copo']},{combo['Preço']}\n")
        print("Item alterado com sucesso!")
    else:
        print("ID de item inválido!")
        return adm()

#Remover Combo do cardapio
def remover_Combo_cardapio():
    mostrar_cardapio()
    id = input("Digite o ID do item que deseja remover: ")
    if id in carregar_cardapio():
        opt= input(''' 
-------------------------------------------------------
|   1   |    Deseja remover o combo: {id}             |
|   2   |    Voltar ao menu                           |
-------------------------------------------------------
''')
        if opt == "1":
            cardapio = carregar_cardapio()
            del cardapio[id]
            with open("cardapio.txt", "w") as file:
                for id, combo in cardapio.items():
                    file.write(f"{id},{combo['Nome']},{combo['Lanche']},{combo['Acompanhamento']},{combo['Copo']},{combo['Preço']}\n")
            print("Item removido com sucesso!")
        elif opt == "2":
            print("Operação cancelada.")
        else:
            print("Opção inválida! Operação cancelada.")
    else:
        print("ID de item inválido!")
        return adm()


# Função para pedir um combo do cardápio
def pedir_combo():
    limpar_tela()
    cardapio = carregar_cardapio()
    mostrar_cardapio()
    escolha = input("Escolha um combo (ex: 1): ")
    if escolha in cardapio:
        carrinho.append((cardapio[escolha]['Nome'], cardapio[escolha]['Preço']))
        print('\n')
        print(Fore.LIGHTYELLOW_EX + "Combo adicionado ao carrinho!! " + Style.RESET_ALL)
        print(f"\n{cardapio[escolha]['Nome']} - R${cardapio[escolha]['Preço']:.2f} adicionado ao carrinho.")
        input("")
    else:
        print("Combo não encontrado.")
        input("")
        main()

# Função para exibir itens
def exibir_itens():
    limpar_tela()
    print(Fore.YELLOW + "ITENS DISPONÍVEIS\n" + Style.RESET_ALL)
    headers = [Fore.LIGHTMAGENTA_EX + "Número", "Item", "Preço" + Style.RESET_ALL ]
    table_data = []
    Exib = LoadTxt("[")
    for item, tipo in Exib.items():
        row = [item, tipo[0], Fore.GREEN + f"R${tipo[1]}" + Style.RESET_ALL]
        table_data.append(row)
    print(tabulate(table_data, headers=headers, tablefmt="psql"))

# Função para montar um pedido personalizado
def Pedir_itens():
    limpar_tela()
    print("Menu de itens Disponiveis")
    Exib = LoadTxt("[")
    exibir_itens()

    opt = input(Fore.CYAN +
            '\n Digite o número do item que gostaria de Adicionar ao seu carrinho (digite 99 para sair): ' + Style.RESET_ALL)
    if opt == "99":
            return
    elif opt.isdigit() and 1 <= int(opt) <= len(Exib):
        item_index = int(opt) - 1
        item_escolha = list(Exib.keys())[item_index]
        nome_item = Exib[item_escolha][0]
        valor_item = Exib[item_escolha][1]
        carrinho.append((nome_item, valor_item))
        print('\n')
        print(Fore.LIGHTYELLOW_EX + "Seu pedido foi adicionado ao carrinho!! "+ Style.RESET_ALL)

        headers = [ "Número", "Item", "Preço"]
        table_data = []
        Exib = LoadTxt("[")

        row = f"{item_escolha}", f"{nome_item}", Fore.GREEN + f"R${valor_item}" + Style.RESET_ALL
        table_data.append(row)
        print(tabulate(table_data, headers=headers, tablefmt="psql"))
        i = input("")
    else:
        input('\nOpção inválida, pressione Enter para tentar novamente.')

# Função para exibir o carrinho
def exibir_carrinho():
    limpar_tela()
    if not carrinho:
        print(Fore.RED + "O carrinho está vazio." + Style.RESET_ALL)
        return
    print(Fore.YELLOW + "CARRINHO\n" + Style.RESET_ALL)
    headers = [Fore.GREEN + "Item", "Preço" + Style.RESET_ALL]
    table_data = []
    total_carrinho = 0
    for nome_lanche, valor_lanche in carrinho:
        row = [nome_lanche, f"R${valor_lanche}"]
        table_data.append(row)
        total_carrinho += float(valor_lanche)
    print(tabulate(table_data, headers=headers, tablefmt="psql"))
    print("\n" + Fore.YELLOW + "Valor Total do Carrinho: " +
          Style.RESET_ALL + f"R${total_carrinho:.2f}")
    i = input('')

# Função para ver e deletar algo do carrinho  
def ver_carrinho():
    limpar_tela()
    if not carrinho:
        print(Fore.RED + "O carrinho está vazio." + Style.RESET_ALL)
        return
    print(Fore.YELLOW + "CARRINHO\n" + Style.RESET_ALL)
    headers = [Fore.GREEN + "Item", "Preço" + Style.RESET_ALL]
    table_data = []
    total_carrinho = 0
    for nome_lanche, valor_lanche in carrinho:
        row = [nome_lanche, f"R${valor_lanche}"]
        table_data.append(row)
        total_carrinho += float(valor_lanche)
    print(tabulate(table_data, headers=headers, tablefmt="psql"))
    print("\n" + Fore.YELLOW + "Valor Total do Carrinho: " +
          Style.RESET_ALL + f"R${total_carrinho:.2f}")
    i = input('')
    print(''' 
-------------------------------------------------------
| Opção |                   Descrição                 |
-------------------------------------------------------
|   1   |    Excluir item ou combo do pedido          |
|   2   |    Voltar ao menu                           |
-------------------------------------------------------
''')
    opçao = input("Digite a opçao que deseja escolher: ")
    if opçao == "1":
        opt = input("\nDigite o número do item que deseja remover (digite 99 para sair): ")
        if opt == "99":
            return
        elif opt.isdigit() and 1 <= int(opt) <= len(carrinho):
            item_index = int(opt) - 1
            del carrinho[item_index]
        print("Item removido do carrinho.")
        exibir_carrinho()
    elif opçao == "2":
        return()  
    else:
        input("\nOpção inválida, pressione Enter para tentar novamente.")

def finalizar_pedido():
    exibir_carrinho()
    print(f''' 
    Sua compra foi finalizada
    sua comanda: {gerar_comanda()}
''' ) 

# Função Gerar comanda
def gerar_comanda():
    letras = string.ascii_uppercase  # Obtém todas as letras maiúsculas de A a Z
    numeros = string.digits  # Obtém todos os dígitos de 0 a 9
    Comanda = ''.join(random.choices(letras + numeros, k=5))  # Escolhe 5 caracteres aleatórios
    return Comanda

# Função limpar tela
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

# classificar atendimento 
def classificar_atendimento():
    print("como classifca o atendimento?")
    print("1. exclente")
    print("2. bom")
    print("3. regular")
    print("4. ruim")

    opcao = input("escolha uma das opções: ")

    if opcao == '1':
        print("voce classificou o atendimento como EXCLENTE!")
    elif opcao == '2':
        print("voce classificou o atendimento como BOM!")
    elif opcao == '3':
        print("voce classificou o atendimento como REGULAR!")
    elif opcao == '4':
        print("voce classificou o atendimento como RUIM! ")
    else:
        print("opção inválida, escolha uma opção válida.")

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

# Executar o programa
aut()