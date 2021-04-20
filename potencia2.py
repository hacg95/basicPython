def run():
    LIMITE = 1000000

    exponente = 0
    potencia_2 = 2**exponente
    while potencia_2 < LIMITE:
        print ("2 elevado " + str(exponente) + " es: " + str(potencia_2))
        exponente += 1
        potencia_2 = 2**exponente
    

if __name__ == "__main__":
    run()