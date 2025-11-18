'''2 - Criar um código que registre as notas de alunos e calcular a média da turma.'''


notas = []

while True:

    entrada = input("Digite uma nota (digite fim para encerrar): \n")

    if entrada.lower() == "fim":
        break

    try: 
        nota = float(entrada)

        if nota >= 0 and nota <= 10:
            notas.append(nota)
        
        else:
            print("Digite uma nota válida.")
    
    except ValueError:
        print("Valor inválido. Digite uma nota válida ou fim")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"A média é de: {media:.2f}")

else:
    print("Nenhuma nota válida registrada")