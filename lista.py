lista = []

while True:
    print("\n1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Remover item")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        item = input("Digite o item: ")
        lista.append(item)

    elif opcao == "2":
        if len(lista) == 0:
            print("Lista vazia")
        else:
            for i, item in enumerate(lista):
                print(i, "-", item)

    elif opcao == "3":
        for i, item in enumerate(lista):
            print(i, "-", item)
        try:
            indice = int(input("Número do item: "))
            lista.pop(indice)
        except:
            print("Erro ao remover.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida")