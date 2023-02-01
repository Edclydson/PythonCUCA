#DESAFIO
cod_produto= int(input("Digite o cod do produto:"))
if (cod_produto==1):
    # COD 1
    print("CODIGO 1 - Alimento não perecível!")
elif(cod_produto<=4):
    # COD 2, 3 OU 4
    print("CODIGO", cod_produto ,"- Alimento perecível!")
elif(cod_produto==5 or cod_produto==6):
    # COD 5 OU 6
    print("CODIGO", cod_produto ,"- Vestuário!")
elif(cod_produto==7):
    #COD 7
    print("CODIGO 7 - Higiene Pessoal!")
elif(cod_produto<=15):
    #COD 8 ATE 15
    print("CODIGO",cod_produto,"- Limpeza e utensilios domesticos!")
else:
    # COD INVALIDO
    print("Codigo Invalido!")

    
