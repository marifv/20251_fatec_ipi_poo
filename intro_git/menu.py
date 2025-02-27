def menu():
    print("-----------Menu de Opções--------------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = soma(num1, num2)
    print("Resultado da soma:", resultado)

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


