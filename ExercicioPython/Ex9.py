def mostrar_tabuada(numero):
    print(f"Tabuada do {numero}:")

    for i in range(1, 11):
        print(f"{numero} * {i:2} = {numero * i}")

numero = int(input("Diga um numero inteiro: "))
mostrar_tabuada(numero)