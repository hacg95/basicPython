def es_primo(numero):
    lista_primos = []
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for x in range(1, numero+1):
            if lista(numero):
                lista_primos.insert(0, x)
            else:
                continue
        lista_primos = lista_primos[::-1]
        for m in lista_primos:
            if (numero/m)<numero:
                if numero % m == 0:
                    return False
                else: 
                    return True
        


def lista(numero):
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
        print(str(numero)+" Es un número primo")
    else:
        print(str(numero)+" No es un número primo")


if __name__ == "__main__":
    run()