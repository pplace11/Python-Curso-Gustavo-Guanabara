def calcular_preco_aluguel():
    km_percorido = float(input("Informe a quantidade de KM percorrido: "))
    dias_alugados = int(input("Informe a quantidade de dias pelos quais o carro foi alugado: "))

    preco_por_km = 0.15
    preco_por_dias = 60
    preco_total_dias = dias_alugados * preco_por_dias
    preco_total_km = km_percorido * preco_por_km
    preco_total = preco_total_dias + preco_total_km

    print(f"Os dia que vc alugou o carro foi {dias_alugados}.")
    print(f"Essa foi a quantidade de andado pelo carro {km_percorido:.2f}km.")
    print(f"O valor a pagar pelo aluguel do carro é {preco_total:.2f}€.")

calcular_preco_aluguel()