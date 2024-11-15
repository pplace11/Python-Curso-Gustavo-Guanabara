def calcular_temperatura():
    celsius = float(input("Diga a sua temperatura em celsius: "))

    fahrenheit = (celsius * 9/5) + 32

    print(f"A temperatura em Celsius é {celsius:.2f}ºC e em Fahrenheit é {fahrenheit:.2f}ºF.")
calcular_temperatura()