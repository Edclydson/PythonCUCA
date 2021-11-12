salario_bruto= float(input("Digite seu salário! R$:"))
if salario_bruto<=3000:
    # SALARIO ABAIXO DE 3000 - 5%
    print("Você recebe menos de R$ 3000, então...")
    salario_liquido= salario_bruto - (salario_bruto * 0.05)
    print("Com o desconto de 5%, o seu salário liquido é: R$",salario_liquido)
elif(salario_bruto>3000 and salario_bruto<=6000):
    # SALARIO ENTRE 3000 E 6000 - 8%
    print("Você recebe entre R$ 3000 e R$ 6000, então...")
    salario_liquido= salario_bruto - (salario_bruto * 0.08)
    print("Com o desconto de 8%, o seu salário liquido é: R$",salario_liquido)
elif(salario_bruto>6000 and salario_bruto<=9000):
    # SALARIO ENTRE 6000 e 9000 - 11%
    print("Você recebe entre R$ 6000 e R$ 9000, então...")
    salario_liquido= salario_bruto - (salario_bruto * 0.11)
    print("Com o desconto de 11%, o seu salário liquido é: R$",salario_liquido)
elif(salario_bruto>9000):
    # SALARIO MAIS DE 9000 - 15%
    print("Você recebe mais de R$ 9000, então...")
    salario_liquido= salario_bruto - (salario_bruto * 0.15)
    print("Com o desconto de 15%, o seu salário liquido é: R$",salario_liquido)
else:
    print("erro")
