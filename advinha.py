# LOOP INFINITO P/ JOGAR O QUANTO QUISER
while(0 < 1):
    print("Responda: 1 para SIM ou 2 para NÃO \n \n")
    quest = int(input("O animal é um mamífero? \n"))
    # MAMIFERO
    if(quest == 1):
        print("Responda: 1 para SIM ou 2 para NÃO \n \n")
        quest = int(input("O animal é quadrúpede? \n"))
        # QUADRUPEDE
        if(quest == 1):
            print("Responda: 1 para SIM ou 2 para NÃO \n \n")
            quest = int(input("O animal é carnívoro?\n "))
            # CARNIVORO
            if(quest == 1):
                print("\nO animal que você pensou foi, Leão!\n")
                # CONDIÇÃO P/ PARAR JOGO OU CONTINUAR APOS UMA RESPOSTA
                print("Responda: 1 para SIM ou 2 para NÃO \n ")
                quest = int(input("Você quer continuar jogando?\n"))
                if(quest == 1):
                    continue
                else:
                    break
            # HERBIVORO
            else:
                print("\nO animal que você pensou foi, Cavalo\n")
                print("Responda: 1 para SIM ou 2 para NÃO \n ")
                quest = int(input("Você quer continuar jogando?\n"))
                if(quest == 1):
                    continue
                else:
                    break
        # BIPEDE
        else:
            print("Responda: 1 para SIM ou 2 para NÃO \n \n")
            quest = int(input("O animal é bípede? \n"))
            if(quest == 1):
                print("Responda: 1 para SIM ou 2 para NÃO \n \n")
                quest = int(input("O animal é onívoro? \n"))
                # ONIVORO
                if(quest == 1):
                    print("\nO animal que você penso foi, Homem!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
                # FRUTIVORO
                else:
                    print("\nO animal qe você pensou foi, Macaco!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
            else:
                print("Responda: 1 para SIM ou 2 para NÃO \n \n")
                quest = int(input("O animal é voador? \n"))
                # VOADOR
                if(quest == 1):
                    print("\nO animal que você pensou foi, Morcego!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
                # AQUATICO
                else:
                    print("\nO animal que você pensou foi, Baleia!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
    else:
        print("Responda: 1 para SIM ou 2 para NÃO \n \n")
        quest = int(input("O animal é uma ave? \n"))
        # AVE
        if(quest == 1):
            print("Responda: 1 para SIM ou 2 para NÃO \n \n")
            quest = int(input("É uma ave não-voadora? \n"))
            # NAO VOADORA
            if(quest == 1):
                print("Responda: 1 para SIM ou 2 para NÃO \n \n")
                quest = int(input("É uma ave tropical? \n"))
                # TROPICAL
                if(quest == 1):
                    print("\nO animal que você pensou foi, Avestruz!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
                # POLAR
                else:
                    print("\nO animal que você pensou foi, Pinguim!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
            else:
                print("Responda: 1 para SIM ou 2 para NÃO \n \n")
                quest = int(input("É nadador? \n"))
                # NADADOR
                if(quest == 1):
                    print("\nO animal que você pensou foi, Pato!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
                # DE RAPINA
                else:
                    print("\nO animal que você pensou foi, Águia!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
        else:
            print("Responda: 1 para SIM ou 2 para NÃO \n \n")
            quest = int(input("O réptil que você pensou, tem casco? \n"))
            # REPTIL
            if(quest == 1):
                print("\nO animal que você pensou foi, Tartaruga!\n")
                print("Responda: 1 para SIM ou 2 para NÃO \n ")
                quest = int(input("Você quer continuar jogando?\n"))
                if(quest == 1):
                    continue
                else:
                    break
            else:
                print("Responda: 1 para SIM ou 2 para NÃO \n \n")
                quest = int(input("É carnívoro? \n"))
                if(quest == 1):
                    print("\nO animal que você pensou foi, Crocodilo!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
                else:
                    print("\nO animal que você pensou foi, Cobra!\n")
                    print("Responda: 1 para SIM ou 2 para NÃO \n ")
                    quest = int(input("Você quer continuar jogando?\n"))
                    if(quest == 1):
                        continue
                    else:
                        break
