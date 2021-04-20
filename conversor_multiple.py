def conversor(message, value):
    quantity = int(input("Ingrese la cantidad en "+message))
    peso = quantity * value 
    peso = str(round(peso,2))
    print("Tienes $"+peso+" pesos colombianos")

selection = int(input("""Escoja una opción: 
1. USD to COP
2. MXN to COP
3. EUR to COP
"""))

if selection == 1:
    conversor("dólares: ", 3594)
elif selection == 2:
    conversor("pesos mexicanos: ", 175)
elif selection == 3:
    conversor("euros: ", 4335)
else:
    print("Selección no valida")