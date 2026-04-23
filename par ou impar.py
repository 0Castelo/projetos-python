while True:
    try:
        numero = int(input("Digite um número (ou 0 para sair): "))
        
        if numero == 0:
            print("Encerrando...")
            break

        if numero % 2 == 0:
            print("Par")
        else:
            print("Ímpar")

    except:
        print("Digite um número válido.")