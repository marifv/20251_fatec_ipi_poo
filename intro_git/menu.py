def menu():
    print("-----------Menu de Opções--------------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair do programa")
    print("---------------------------------------")

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Impossível dividir por zero, escolha outro número"
    return a / b

while True:
    menu()  

    opcao = int(input("Digite a opção desejada: "))  

    if opcao == 1:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = soma(num1, num2)
        print("Resultado da soma: ", resultado)

    elif opcao == 2:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = subtracao(num1, num2)
        print("Resultado da subtração: ", resultado)

    elif opcao == 3:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = multiplicacao(num1, num2)
        print("Resultado da multiplicação: ", resultado)

    elif opcao == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = divisao(num1, num2)
        print("Resultado da divisão: ", resultado)

    elif opcao == 0:
        print("Obrigado por usar nosso Menu-Calculadora!")
        break  

    else:
        print("Esse número não existe, use um número de 0 a 4 conforme a opção desejada")


