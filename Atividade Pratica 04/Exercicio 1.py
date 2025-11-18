'''
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
'''

while True:
    try:

        num1 = float(input("Digite o primeiro valor: \n"))
        num2 = float(input("Digite o segundo valor: \n"))

        operacao = input("Digite a operação desejada (+, -, * ou /)")

        if operacao == "+":
            resultado = num1 + num2
        
        elif operacao == "-":
            resultado = num1 - num2
        
        elif operacao == "*":
            resultado = num1 * num2

        elif operacao == "/":
            if num2 == 0:
                print("Não é possivel dividir um numero por zero.")
                continue
            resultado = num1 / num2
        
        print(f"O resultado é: {resultado}")
        break

    except ValueError:
        print("Por favor, digite valores válidos.")

