""" 3 passadas em todo o texto

- 1ª passada:
    - O caracteres maiusculos e minusculos devem deslocar 3 posições pr a direita baseando a tabela ASCII. Ex: 'a' vira 'd' e y 'y' vira '|'

- 2ª passada:
    -Inverter linha
- 3ª passada:
    - TOdos os caracteres da metade em diante (truncada) devem mudar posição pra esquerda baseando a tabela ASCII. Ex: 'b' vira 'a' e 'a' vira '´'

 """

n = int(input())

for i in range(n):
    texto = input()

    
    texto1 = ""
    for c in texto:
        if c.isalpha():
            texto1 += chr(ord(c) + 3)
        else:
            texto1 += c

    
    texto2 = texto1[::-1]

    
    metade = len(texto2) // 2
    
    parte_inicial = texto2[:metade] 
    parte_final = ""
    
    
    for c in texto2[metade:]:
        parte_final += chr(ord(c) - 1)

    texto_final = parte_inicial + parte_final
    print(texto_final)