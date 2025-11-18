'''2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
'''

def palindromo(texto):
    texto = texto.lower()
    texto_formatado = ''.join(c for c in texto if c.isalnum())
    
    if texto_formatado == texto_formatado[::-1]:
        return "Sim"
    else:
        return "Não"


texto = input("Digite uma palavra ou frase: ")

verifica_texto = palindromo(texto)

print(verifica_texto)