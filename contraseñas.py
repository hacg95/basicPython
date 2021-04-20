import random


def create_pass():
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Z"]
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    caracteres = mayusculas + minusculas + numeros
    password = []
    
    for i in range(10):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)
    
    password = "".join(password)
    return password


def run():
    password = create_pass()
    print("Tu nueva contraseña es: "+password)

if __name__ == "__main__":
    run()