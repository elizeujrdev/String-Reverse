def inverter_string(string):
    inverted = ''
    for char in string:
        inverted = char + inverted
    return inverted

texto = input("Digite uma string: ")
texto_invertido = inverter_string(texto)
print("String invertida:", texto_invertido)