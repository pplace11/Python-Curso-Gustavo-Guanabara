def converter_euros_para_dolares():
    taxa_cambio = 1.10

    quantidade_eu = float(input(f"Diga a quantidade de dinheiro tem na carteira (EU): "))
    quantidade_usd = quantidade_eu*taxa_cambio

    print(f"Com {quantidade_eu:.2f}€, voce pode comprar US${quantidade_usd:.2f}")

converter_euros_para_dolares()