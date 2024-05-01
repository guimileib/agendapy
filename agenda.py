# Agenda para salvar; editar; deletar e marcar um contato como favorito

# funções que vai interligar com o if-else
def salvar_contato(contatos,nome_contato,numero, email):#1
    contato = {"nome":nome_contato, "telefone":numero, "email":email, "favorito": False}
    contatos.append(contato)
    print(f"\n O contato de {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):#2
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start = 1):
        status = "★" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        numero = contato["telefone"]
        print(f"{indice}. {status} Nome: {nome_contato} \n Telefone: {numero} \n Email: {email}")
    return

def editar_contato(contatos, indice_contato, novo_nome_contato):#3
    indice_contato_ajustado = int(indice_contato - 1)
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado] ["nome"] = novo_nome_contato
        contatos[indice_contato_ajustado] ["telefone"] = novo_numero_contato
        contatos[indice_contato_ajustado] ["email"] = novo_email_contato
        print("=====================================================")
        print(f"\nContato {nome_contato} foi modificado com sucesso!")
        print("=====================================================")
    else:
        print("\nContato não foi encontrado na sua agenda.")
    return

def favoritar_contato(contatos, indice_contato):#4
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} foi favoritado.")
    return

def deletar_contato(contatos, indice_contato):#6
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        for contato in contatos: 
            contatos.remove(contato) 
        print("=====================================================")
        print(f"Contato {nome_contato} foi deletado com sucesso!")
        print("=====================================================")
    return



# lista de contatos:
contatos = []

# Menu
while True:
    print("\nMenu Agenda de Contatos:")
    print("1. Adicionar um novo contato")
    print("2. Ver agenda de contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Deletar contato")
    print("6. Sair da agenda")
    
    escolha = input("\nDigite a sua escolha: ")
    
    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja salvar: ")
        numero = int(input("Digite o número do contato que deseja salvar: "))
        email = input("Digite o email do seu contato: ")
        salvar_contato(contatos, nome_contato, numero, email)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = int(input("Selecione a partir do indice do contato que deseja editar: "))
        novo_nome_contato = input("Digite o novo nome do Contato: ")
        novo_numero_contato = int(input("Digite o novo número do Contato: "))
        novo_email_contato = input("Digite o novo email do Contato: ")
        editar_contato(contatos, indice_contato, novo_nome_contato)
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Selecione a partir do indice do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)
    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = int(input("Selecione a partir do indice do contato que deseja deletar: "))
        for contato in contatos:
            if contato["favorito"]:
                decisao = input("Deseja excluir esse contato? Digite sim ou não, como resposta: ")
                if decisao.upper() == "SIM":
                    deletar_contato(contatos, indice_contato)
                else:
                   ver_contatos(contatos)
                        
    elif escolha == "6":
        break    
    
        
    