def caucular_aumento_salario():
    salario = float(input(f"Fala o salario do seu funcionario: "))

    aumento = salario*0.15
    novo_salario = salario+aumento

    print(f"Esse era o salario sem o aumento: {salario:.2f}€")
    print(f"Esse é o novo salario com aumento: {novo_salario:.2f}€")

caucular_aumento_salario()