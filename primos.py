def es_primo(numero):
    if numero==1:
        return False
    else:
        n = 0
        for i in range(1, numero+1):
            if i==1 or i==numero:
                continue
            if numero % i == 0:
                n+=1
        if n==0:
            return True
        else:
            return False


def run():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es un número primo")
    else:
        print("No es un número primo")


if __name__ == "__main__":
    run()