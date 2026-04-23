def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def menu():
    print("\nCalculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Saindo...")
        break

    try:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
    except:
        print("Entrada inválida.")
        continue

    if opcao == "1":
        print("Resultado:", soma(num1, num2))
    elif opcao == "2":
        print("Resultado:", subtracao(num1, num2))
    elif opcao == "3":
        print("Resultado:", multiplicacao(num1, num2))
    elif opcao == "4":
        print("Resultado:", divisao(num1, num2))
    else:
        print("Opção inválida.")