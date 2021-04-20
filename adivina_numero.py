import random


def run():
    numero_random = random.randint(1, 100)
    numero_elegido = int(input("Ingresa un número entre el 1 y el 100: "))
    vidas = 5
    while numero_elegido != numero_random:
        vidas -= 1
        print("Vidas restantes: "+str(vidas))
        if vidas == 0:
            print("Perdiste :(")
            break
        if numero_elegido<numero_random:
            numero_elegido = int(input("Ingresa un número mayor: "))
        elif numero_elegido>numero_random:
            numero_elegido = int(input("Ingresa un número menor: "))
    if numero_elegido == numero_random:
        print("Ganaste :)")


if __name__ == "__main__":
    run()