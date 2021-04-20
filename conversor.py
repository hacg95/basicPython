pesos = input("¿Cuántos pesos tienes? ")
pesos = float(pesos)
valor_dolar = 3594
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
