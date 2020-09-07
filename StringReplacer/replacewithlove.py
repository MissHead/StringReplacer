def replacewithlove(texto):
    texto_final = ''
    lista = texto.split(',')
    for palavra in lista:
        if 'odiar' in palavra:
            texto_final += palavra + ' ❤ '
        if 'amor' in palavra:
            texto_final += palavra + ' ¯|_(ツ)_|¯ '
    return texto_final


texto = input()
print(replacewithlove(texto))
