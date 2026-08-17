print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo(a) ilha do tesouro!!")
print("Sua missão é achar o tesouro!.")
direcao = input('Você está caminhando pela floresta, para aonde você quer ir? insira "Esquerda" ou "Direita": ')
if direcao == "Direita":
    print("Você caiu em uma armadilha de goblins! Fim de jogo.")
elif direcao == "Esquerda":
    lago = input('Você chegou em um porto e precisa atravessar o Lago Creek. Você deseja esperar um bote ou atravessar nadando\nInsira "Nadar" ou "Esperar": ')
    if lago == "Nadar":
        print("Ao tentar atravessar nadando você foi devorado pelo Monstro do Lago Creek! Fim de jogo.")
    elif lago == "Esperar":
        porta = input('Você chega em uma caverna, onde há três portas: Azul, Vermelha e Amarela. Qual dessas portas você deseja entrar?\nInsira "Vermelha", "Amarela" ou "Azul": ')
        if porta == "Vermelha":
            print("Você abre a porta e recebe uma enorme onda de calor, você pega fogo! Fim de jogo.")
        elif porta == "Azul":
            print("Você abre a porta e se depara com um enorme dragão, ele nota sua presença! Fim de jogo.")
        elif porta == "Amarela":
            print("PARABÉNS!!! VOCÊ ENCONTROU O GRANDE TESOURO!")
        else:
            print("Você escolheu uma opção inválida!")
    else:
        print("Você escolheu uma opção inválida!")
else:
    print("Você escolheu uma opção inválida!")