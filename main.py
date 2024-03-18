def inverte_string(string):
    return string[::-1]

texto = input("Digite uma string: ")
texto_invertido = inverte_string(texto)
print("String invertida:", texto_invertido)