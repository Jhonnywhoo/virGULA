'''
Trabalho MINI-CRUD a pedido do Professor Luiz.

Nosso CRUD propõe criar uma ferramenta de gestão e atendimento para um restaurante fast-food baseado em cardápio de combos e alguns itens.

Jhonny Wendel Oliveira de Brito - 1D ADS
Gustavo de Freitas Andrade - 1D ADS
Enzo Reis Bernardino - 1D ADS
Alex Michel Facciolla da Silva - 1D ADS
'''

import os
import pwinput
import random
import string
from tabulate import tabulate
from colorama import Fore, Style

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
            finalizar_pedido()
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
|   1   |    Modificar cardápio de COMBOS             |
|   2   |    Modificar cardápio de ITENS              |
|   3   |    Alterar USUÁRIO administrador            |
|   4   |    Alterar SENHA administrador              |
|   5   |    Sair                                     |
-------------------------------------------------------
\n
''')
        opcao=input("ENTRE COM O NÚMERO DE UMA DAS OPÇÕES ACIMA: ")
        if opcao == "1":
            PainelCombo()
            return()
        elif opcao == "2":
            PainelItens()
            return()
        elif opcao == "3":
            AltAdm()
            return()
        elif opcao == "4":
            AltSenhaAdm()
            return()
        elif opcao == "5":
            aut()
            return()
        else:
            limpar_tela()
            input("\nOpção inválida, tente novamente.")
            
def PainelCombo():
    limpar_tela()
    mostrar_cardapio()
    print('''
-------------------------------------------------------
| Opção |                  Descrição                  |
-------------------------------------------------------
|   1   |    Adicionar combo ao cardápio              |
|   2   |    Remover combo do cardápio                |
|   3   |    Alterar combo do cardápio                |
|   4   |    Voltar                                   |
-------------------------------------------------------
\n
''')
    opt=input("ENTRE COM O NÚMERO DE UMA DAS OPÇÕES ACIMA: ")
    if opt == "1":
        adicionar_ao_cardapio()
        return ()
    elif opt == "2":
        remover_Combo_cardapio()
        return ()
    elif opt == "3":
        alterar_do_Cardapio()
        return ()
    elif opt == "4":
        return adm()
        return ()
            
def PainelItens():            
    limpar_tela()
    exibir_itens()
    print('''
-------------------------------------------------------
| Opção |                  Descrição                  |
-------------------------------------------------------
|   1   |    Adicionar ITEM ao menu                   |
|   2   |    Remover ITEM do menu                     |
|   3   |    Alterar ITEM do menu                     |
|   4   |    Voltar                                   |
-------------------------------------------------------
\n
''')
    opt=input("ENTRE COM O NÚMERO DE UMA DAS OPÇÕES ACIMA: ")
    if opt == "1":
        AddItem()
        return()
    elif opt == "2":
        RemItem()
        return()
    elif opt == "3":
        AltUnid()
        return()
    elif opt == "4":
        adm()
        return()
    else:
        input("OPÇÃO INVÁLIDA. Pressione Enter para tentar novamente.")
        adm()
        return()

# Função para autenticação
def aut():
    limpar_tela()
    Logo()
    usuario = input('''
BEM VINDO!
Nome (Entre "admin" para funções CRUD ou "fechar" para sair): ''')
    if usuario == "fechar":
        return()
    Login = LoadTxtL() # Carrega os dados dentro da função aut
    for login,valores in Login.items():
        if usuario == valores[0]:
            senha = pwinput.pwinput(prompt='''
ADMINISTRADOR (Digite FIM para sair)
Senha (1234): ''')
            if senha.lower() == "fim":
                return aut()
            elif senha == valores[1]:
                return adm()
            else:
                while senha not in valores[1]:
                    limpar_tela()
                    senha = pwinput.pwinput(prompt='''
SENHA INCORRETA (digite FIM para sair)
Senha: ''')
                    if senha.lower() == "FIM":
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
    Login = LoadTxtL()
    usuario_teste=input("Digite o usuário administrador atual: ")
    for login,dados in Login.items():
        while usuario_teste not in dados[0]:
            print("\nUsuário administrador incorreto, tente novamente (digite FIM para cancelar).")
            usuario_teste=input("\nDigite o usuário administrador atual: ")
            if usuario_teste.lower() == "fim":
                return adm()
        if usuario_teste == dados[0]:
            usuario_novo = input("Digite o novo usuário administrador: ")
            while '.' in usuario_novo: # para evitar conflitos no .txt
                input("O usuário não pode conter ponto(.), tente novamente: ")
            Login["login"]=[usuario_novo,dados[1]]
            SaveTxtL(Login)
            input("\nSalvo com sucesso! Pressione enter para continuar")
            return adm()

# Função para alterar senha de administrador
def AltSenhaAdm():
    limpar_tela()
    Login = LoadTxtL()
    senha_teste = input("Digite a senha atual: ")
    for login,dados in Login.items():
        while senha_teste not in dados[1]:
            limpar_tela()
            print("Senha incorreta, tente novamente. (digite FIM para sair).\n")
            senha_teste = input("Digite a senha atual: ")
            if senha_teste.lower() == "FIM":
                return adm()
        if senha_teste in dados[1]:
            limpar_tela()
            nova_senha = input("Digite a nova senha: ")
            while '.' in nova_senha: # Para evitar conflitos no .txt
                nova_senha = input("A senha não pode conter ponto(.), tente novamente: ")
            Login["login"]=[dados[0],nova_senha]
            SaveTxtL(Login)
            input("\nSalvo com sucesso! Pressione enter para continuar")
            return adm()

# Funções para alterar preço de unidade do montar pedido
def AltUnid():
    limpar_tela()
    print('''
Aqui é possível alterar o nome e o preço dos itens disponíveis no menu "Escolher apenas 1 item" dos clientes.
As alterações são salvas automaticamente no arquivo "main.txt".
''')
    exibir_itens()
    Alt = LoadTxt()
    opt = input('Digite o número do item que gostaria de alterar (digite FIM para sair): ')
    if opt.lower() == "fim":
        return adm()
    elif opt.isdigit() and int(opt) <= len(Alt): # filtro para a escolha ser dígito e estar na length no cardápio
        alterar_item(list(Alt.keys())[int(opt) -1], Alt) # carrega a outra função já com parmetros de lista, excluir primeira linha e variável Alt
    else:
        input('\nOpção inválida, pressione Enter para tentar novamente.')
        AltUnid()
        return()

def alterar_item(item, Alt):
    limpar_tela()
    precoatt=Alt[item][1]
    print(f''' 
{item}:
--------------------------------------------
   1   |  {Alt[item][0]}                            
   2   |  R${FormatReal(precoatt)}                            
--------------------------------------------
''')
    alteracao = input('\nDigite o número do que gostaria de alterar (Digite FIM para cancelar): ')
    if alteracao.lower() == "fim":
        AltUnid()
        return()
    elif alteracao == "1":
        nome = input(f"\nDigite o novo nome que gostaria de registrar para {item} (Digite FIM para cancelar): ")
        if nome.lower() == "fim":
            return AltUnid()
        Alt[item][0] = nome
    elif alteracao == "2":
        preco = input('''\nDigite o novo preço que gostaria de registrar
(sem cifrão, apenas número e virgula)
Digite FIM para cancelar: ''')
        if preco.lower() == "fim":
            return AltUnid()
        while not preco.replace(",","").isdigit():
            preco = input('''\nPREÇO INVÁLIDO.
Digite o novo preço que gostaria de registrar (sem cifrão, apenas número e ponto)
Digite FIM para cancelar: ''')
            if preco.lower() == "fim":
                return AltUnid()
                return ()
        precoatt = preco.replace(",",".")
        Alt[item][1] = precoatt
    else:
        limpar_tela()
        input("opção não encontrada. Pressione Enter para tentar novamente.")
        alterar_item(item,Alt)
        return ()
    SaveTxt(Alt)
    input("\nSalvo!")
    return AltUnid()

# Função para adicionar item
def AddItem():
    Alt=LoadTxt()
    exibir_itens()
    opt=input("\nPressione Enter para adicionar um item a lista ou entre FIM para cancelar: ")
    if opt.lower() == "fim":
        return PainelItens()
        return ()
    limpar_tela()
    exibir_itens()
    nome=input("\nDigite o nome do novo item: ")
    preco=input("Digite o preço do novo item, sem cifrão, apenas número s virgula: ")
    while not preco.replace(",","").isdigit():
        print("\nPREÇO INVÁLIDO, TENTE NOVAMENTE.")
        preco=input("Digite o preço do novo item, sem cifrão, apenas número e virgula: ")
    limpar_tela()
    exibir_itens()
    c=input(f'''

DESEJA ADICIONAR ESSE ITEM NA LISTA?
----------------------------
{nome}  |  R${preco}                            
----------------------------

Pressione Enter para confirmar ou entre FIM para cancelar: ''')
    if c.lower() == "fim":
        return AddItem()
        return ()
    else:
        precoatt = preco.replace(",",".")
        AltAtt = {str(len(Alt) +1):[nome,precoatt]}
        Alt.update(AltAtt)
        SaveTxt(Alt)
        input("\nSalvo!")
        return PainelItens()
        return ()
 
# Remover Item 
def RemItem():
    Alt = LoadTxt()
    limpar_tela()
    exibir_itens()
    opt = input("\nEntre com o número do que gostaria de deletar ou FIM para cancelar: ")
    if opt.lower() == "fim":
        return PainelItens()
    elif opt.isdigit() and int(opt) <= len(Alt):
        index = list(Alt.keys())[int(opt) -1]
        print(f'''
Deseja deletar o item:
{index} | {Alt[index][0]} | R${FormatReal(Alt[index][1])}
''')
        c = input("Pressione Enter para confirmar ou entre FIM para cancelar: ")
        if c.lower() == "fim":
            return PainelItens()
        else:
            Alt.pop(opt)
            SaveTxt(Alt)
            input("\nSalvo!")
            return PainelItens()
    else:
        input('\nOpção inválida, pressione Enter para tentar novamente.')
        return RemItem()
 
# Carregar_cardapio
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
        a=combo['Preço']
        row = [num, combo['Nome'], combo['Lanche'], combo['Acompanhamento'], combo['Copo'], f"R${FormatReal(a)}"]
        table_data.append(row)
    print(tabulate(table_data, headers=headers, tablefmt="psql"))

#Adicionar item ao cardapio
def adicionar_ao_cardapio():
    limpar_tela()
    mostrar_cardapio()
    nome = input("\nDigite o nome do novo item: ")
    lanche = input("Digite o tipo de recheio do lanche (ex: Carne): ")
    acompanhamento = input("Digite o acompanhamento: ")
    copo = input("Digite o tamanho do copo (ex: 200ml): ")
    preco = input("Digite o preço do item sem cifrão, apenas número e virgula: ")
    while not preco.replace(",","").isdigit():
        preco = input("\nPREÇO INVÁLIDO, tente novamente: ")
    limpar_tela()
    mostrar_cardapio()
    c=input(f'''
Deseja adicionar o combo:
| {nome},  {lanche},  {acompanhamento},  {copo},  R${preco} |
ao cardápio de combos?

Enter para confirmar ou entre FIM para cancelar: ''')
    if c.lower() == "fim":
        input("\nCancelado!")
        PainelCombo()
        return()
    with open("cardapio.txt", "a") as file:
        precoatt = preco.replace(",",".")
        id = str(len(carregar_cardapio()) + 1)
        file.write(f"{id},{nome},{lanche},{acompanhamento},{copo},{precoatt}\n")
        input("\nItem adicionado ao cardápio!")
    PainelCombo()
    return()

#Alterar combo do cardapio 
def alterar_do_Cardapio():
    limpar_tela()
    mostrar_cardapio()
    id = input("Digite o ID do item que deseja alterar: ")
    if id in carregar_cardapio():
        nome = input("Digite o novo nome do item: ")
        lanche = input("Digite o novo recheio do lanche (ex: Carne): ")
        acompanhamento = input("Digite o novo acompanhamento: ")
        copo = input("Digite o novo tamanho do copo (ex: 200ml): ")
        preco = input("Digite o novo preço do item, sem cifrão, apenas números e virgula: ")
        while not preco.replace(",","").isdigit():
            preco = input('''
PREÇO INVÁLIDO, TENTE NOVAMENTE.
Digite o novo preço do item, sem cifrão, apenas números e virgula: ''')
        precoatt=preco.replace(",",".")
        cardapio = carregar_cardapio()
        cardapio[id] = {'Nome': nome, 'Lanche': lanche, 'Acompanhamento': acompanhamento, 'Copo': copo, 'Preço': precoatt}
        with open("cardapio.txt", "w") as file:
            for id, combo in cardapio.items():
                file.write(f"{id},{combo['Nome']},{combo['Lanche']},{combo['Acompanhamento']},{combo['Copo']},{combo['Preço']}\n")
        input("Item alterado com sucesso!")
    else:
        input("ID de item inválido! Enter para tentar novamente.")
        alterar_do_Cardapio()
        return()
    adm()
    return()

#Remover Combo do cardapio
def remover_Combo_cardapio():
    limpar_tela()
    mostrar_cardapio()
    id = input("Digite o ID do item que deseja remover: ")
    if id in carregar_cardapio():
        limpar_tela()
        mostrar_cardapio()
        opt= input(f''' 
| OPÇÃO |
------------------------------------
|   1   |    Remover o combo: {id}                 
|   2   |    Voltar ao menu                           
------------------------------------
Entre com a opção desejada: ''')
        if opt == "1":
            cardapio = carregar_cardapio()
            del cardapio[id]
            with open("cardapio.txt", "w") as file:
                for id, combo in cardapio.items():
                    file.write(f"{id},{combo['Nome']},{combo['Lanche']},{combo['Acompanhamento']},{combo['Copo']},{combo['Preço']}\n")
            input("\nItem removido com sucesso!")
        elif opt == "2":
            input("Operação cancelada. Enter para voltar.")
        else:
            print("Opção inválida! Operação cancelada.")
    else:
        limpar_tela()
        input("ID de item inválido! Tente novamente.")
        return remover_Combo_cardapio()
    PainelCombo()
    return()


# Função para pedir um combo do cardápio
def pedir_combo():
    limpar_tela()
    cardapio = carregar_cardapio()
    mostrar_cardapio()
    escolha = input("Escolha um combo (ex: 1): ")
    if escolha in cardapio:
        carrinho.append((cardapio[escolha]['Nome'], cardapio[escolha]['Preço']))
        preco=cardapio[escolha]['Preço']
        print('\n')
        print(Fore.LIGHTYELLOW_EX + "Combo adicionado ao carrinho!! " + Style.RESET_ALL)
        print(f"\n{cardapio[escolha]['Nome']} - R${FormatReal(preco)} adicionado ao carrinho.")
        input("")
    else:
        print("Combo não encontrado.")
        input("")
    return()

# Função para exibir itens
def exibir_itens():
    limpar_tela()
    print(Fore.YELLOW + "ITENS DISPONÍVEIS\n" + Style.RESET_ALL)
    headers = [Fore.LIGHTMAGENTA_EX + "Número", "Item", "Preço" + Style.RESET_ALL ]
    table_data = []
    Alt = LoadTxt()
    for item, tipo in Alt.items():
        preco=tipo[1]
        row = [item, tipo[0], Fore.GREEN + f"R${FormatReal(preco)}" + Style.RESET_ALL]
        table_data.append(row)
    print(tabulate(table_data, headers=headers, tablefmt="psql"))

# Função para montar um pedido personalizado
def Pedir_itens():
    limpar_tela()
    print("Menu de itens Disponiveis")
    Alt = LoadTxt()
    exibir_itens()

    opt = input(Fore.CYAN +
            '\n Digite o número do item que gostaria de Adicionar ao seu carrinho (digite FIM para sair): ' + Style.RESET_ALL)
    if opt.lower() == "fim":
        limpar_tela()
        return
    elif opt.isdigit() and 1 <= int(opt) <= len(Alt):
        item_index = int(opt) - 1
        item_escolha = list(Alt.keys())[item_index]
        nome_item = Alt[item_escolha][0]
        valor_item = Alt[item_escolha][1]
        carrinho.append((nome_item, valor_item))
        print('\n')
        print(Fore.LIGHTYELLOW_EX + "Seu pedido foi adicionado ao carrinho!! "+ Style.RESET_ALL)

        headers = [ "Número", "Item", "Preço"]
        table_data = []
        Alt = LoadTxt()
        row = f"{item_escolha}", f"{nome_item}", Fore.GREEN + f"R${FormatReal(valor_item)}" + Style.RESET_ALL
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
        row = [nome_lanche, f"R${FormatReal(valor_lanche)}"]
        table_data.append(row)
        total_carrinho += float(valor_lanche)
    print(tabulate(table_data, headers=headers, tablefmt="psql"))
    print("\n" + Fore.YELLOW + "Valor Total do Carrinho: " +
          Style.RESET_ALL + f"R${FormatReal(total_carrinho)}")

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
        row = [nome_lanche, f"R${FormatReal(valor_lanche)}"]
        table_data.append(row)
        total_carrinho += float(valor_lanche)
    print(tabulate(table_data, headers=headers, tablefmt="psql"))
    print("\n" + Fore.YELLOW + "Valor Total do Carrinho: " +
          Style.RESET_ALL + f"R${FormatReal(total_carrinho)}")
    
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
        opt = input("\nDigite o número do item que deseja remover (digite FIM para sair): ")
        if opt.lower() == "fim":
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
    input("Pressione Enter")

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
    
def LoadTxtL(tipo='todos'):
    L0=[] # Lista que recebrá TXT
    L1={} # DCT que receberá a lista
    with open("login.txt",'r') as Dados:
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

def SaveTxtL(Dict):
    with open("login.txt", 'w') as Dados:
        for chave,dados in Dict.items():
            Dados.write(f"{chave},{dados[0]},{dados[1]}\n")
            
# Função para fornatar moeda
def FormatReal(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

# Executar o programa
aut()