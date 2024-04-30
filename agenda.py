# Agenda para salvar; editar; deletar e marcar um contato como favorito

# funções que vai interligar com o if-else
def salvar_contato(nome_contato,contato ):
    contato = {"Nome:":nome_contato, "Número:":contato}
    contatos.append(contato)
    print(f"\n O contato de {nome_contato} foi adicionado com sucesso!")
    return
def ver_contatos(contatos,elemento):
    print("\nLista de contatos:")
    for elemento in contatos:
        print(elemento)
    return

def editar_contato(contato):
    return

def deletar_contato(contato):
    return

def favoritar_contato(contato):
    return

# lista de contatos:
contatos = []

# Menu
while True:
    print("\nMenu Agenda de Contatos:")
    print("1. Adicionar um novo contato")
    print("2. Ver agenda de contatos")
    print("3. Editar contato")
    print("4. Deletar contato")
    print("5. Favoritar contato")
    print("6. Sair da agenda")
    
    escolha = input("\nDigite a sua escolha: ")
    
    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja salvar: ")
        contato = int(input("Digite o número do contato que deseja salvar: "))
        salvar_contato(nome_contato, contato)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "6":
        break    
    
        
    