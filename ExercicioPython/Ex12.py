def calcular_desconto():
    preco = float(input(f"Diga preço: "))

    desconto = preco * 0.05
    novo_preco = preco - desconto

    print(f"O valor sem o desconto é {preco:.2f}€")
    print(f"O valor com desconto é {novo_preco:.2f}€")

calcular_desconto()