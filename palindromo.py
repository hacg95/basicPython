def palindrom(palabra):
    palabra = palabra.replace(" ", "").lower()
    reves = palabra[::-1]
    if palabra == reves:
        print("Es un palindromo")
    else:
        print("No es un palindromo")


def run():
    print ("¿Quiere conocer si una palabra es un palindromo?")
    palindrom(input("Ingrese una palabra: "))


if __name__ == "__main__":
    run()