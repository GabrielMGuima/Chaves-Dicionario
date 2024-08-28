Cliente = {
    'Clientes':[ ]
}

def adicionar_cliente():

    nome = input('\n Digite seu Nome Completo ==')
    email = input(' Digite seu e-mail ==')
    telefone = input(' Digite Seu telefone  ==')
    endereco = input(' Digite seu endereço ==')
    
    for verificar_cliente in Cliente['Clientes']:
        if verificar_cliente.get("E-mail") == email:
            print(" já existe um Cliente cadastrado com esse e-mail. Não será adicionado novamente.")
            return

    lista_interna = {
        "Nome": nome,
        "E-mail": email,
        "Telefone": telefone,
        "Endereço": endereco
    }
   
    Cliente['Clientes'].append(lista_interna)
    print("\n Cliente adicionado com sucesso!")

def exibir_clientes():

    print("\n  Clientes cadastrados: \n")

    for cliente in Cliente['Clientes']:
        print(f"  Nome: {cliente['Nome']} E-Mail: {cliente['E-mail']} Telefone: {cliente['Telefone']} Endereço: {cliente['Endereço']}")
       # print("-" * 100) #Se Remover de Comentario colocarar linhas potilhadas entre os clientes

def buscar_cliente():

    buscar_email = input("\nDigite o e-mail do cliente que deseja buscar: ")
    for cliente in Cliente['Clientes']:
        if cliente['E-mail'] == buscar_email:
            print("\nCliente encontrado:\n")
            print(f"  Nome: {cliente['Nome']} E-Mail: {cliente['E-mail']} Telefone: {cliente['Telefone']} Endereço: {cliente['Endereço']}")

        else:
            print('\n Cliente Não encontrato!!!')    
        return
    
def remover_cliente():

    email_remocao = input("\n Digite o e-mail do cliente que deseja remover: ")
    for chave, cliente in enumerate(Cliente['Clientes']):
        if cliente['E-mail'] == email_remocao:
            print(f"\nO Cliente De Nome: {cliente['Nome']} Foi Encontrado E Removido")
            del Cliente['Clientes'][chave]
            
            return
    print("\n Cliente não encontrado.")


while True:
    
    opcao = input('''
    1 adicionar clientes
    2 exibir clientes
    3 buscar clinete com o email
    escolha: ''')
    if opcao == '1':
        adicionar_cliente()
    if opcao == '2':
        exibir_clientes()
    if opcao == '3':
        buscar_cliente()
    if opcao == '4':
        remover_cliente()    
    elif opcao != '1' and opcao != '2' and opcao != '3':
        print("\n Opção invalida!!")