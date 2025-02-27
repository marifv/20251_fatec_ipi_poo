def menu():
    print("-----------Menu de Opções--------------")
    print("1 - Soma")

def soma(a, b):
    return a + b

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = soma(num1, num2)
    print("Resultado da soma:", resultado)


