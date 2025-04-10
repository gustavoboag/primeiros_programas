#inicio da calculadora
print("calculadora simples")
print("as operações são: soma, subtração, multiplicação, divisão e resto da divisão")
#escolha a operação
operacao = input("digite a operação que deseja realizar: ")
# escolha os numeros
num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))
# operaçõa if , elif e else
if operacao == "soma":
    print("o resltado da soma dos dois numeros são:", num1 + num2)

elif operacao == "subtração":
    print("o resltado da subtração dos dois numeros são:", num1 - num2)
elif operacao == "multiplicação":
    print("o resltado da multiplicação dos dois numeros são:", num1 * num2)
elif operacao == "divisão":
    print("o resltado da divisão dos dois numeros são:", num1 / num2)
elif operacao == "resto da divisão":
    print("o resltado do resto da divisão dos dois numeros são:", num1 % num2)
else:
    print("operação inválida")