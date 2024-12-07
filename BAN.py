#Por si só, já é autoexplicativo que é um banco de dados.

def criar_banco():
    banco = {}
    return banco

def adicionar_nome(banco, nome):
    id_usuario = len(banco) + 1
    banco[id_usuario] = nome
    print(f"Nome '{nome}' adicionado com sucesso!")

def listar_nomes(banco):
    if len(banco) == 0:
        print("Nenhum nome encontrado.")
    else:
        print("Lista de nomes:")
        for id_usuario, nome in banco.items():
            print(f"{id_usuario}: {nome}")

def remover_nome(banco, id_usuario):
    if id_usuario in banco:
        del banco[id_usuario]
        print(f"Nome removido com sucesso!")
    else:
        print(f"ID {id_usuario} não encontrado.")



def main():
    banco = criar_banco()
    
    while True:
        print("\n1. Adicionar Nome")
        print("2. Listar Nomes")
        print("3. Remover Nome")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome a ser adicionado: ")
            adicionar_nome(banco, nome)
        elif opcao == '2':
            listar_nomes(banco)
        elif opcao == '3':
            try:
                id_usuario = int(input("Digite o ID do nome a ser removido: "))
                remover_nome(banco, id_usuario)
            except ValueError:
                print("Por favor, digite um ID válido.")
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()