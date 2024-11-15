def calcular_tinta():
    largura = float(input(f"Diga a largura: "))
    altura = float(input(f"Diga a altura: "))

    area = largura*altura
    litro_tinta = area/2

    print(f"A area da parede é {area} metro quadrado.")
    print(f"Voce pricisará de {litro_tinta} litro de tinta para pintar a parede.")

calcular_tinta()