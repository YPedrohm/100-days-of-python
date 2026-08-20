import random
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

escolha = int(input("0: pedra, 1: papel, 2: tesoura\nEscolha sua jogada: "))

if escolha == 0:
    print(pedra)
elif escolha == 1:
    print(papel)
elif escolha == 2:
    print(tesoura)
else:
    print("jogada invalida!")
    exit()

print("O computador escolheu: ")
computador = [pedra, papel, tesoura]
escolhaCPU = random.randint(0, 2)
print(computador[escolhaCPU])

if escolha == 0 and escolhaCPU == 0:
    print("Empate")
elif escolha == 0 and escolhaCPU == 1:
    print("Computador ganhou!")
elif escolha == 0 and escolhaCPU == 2:
    print("Você ganhou!")
elif escolha == 1 and escolhaCPU == 0:
    print("Você ganhou!")
elif escolha == 1 and escolhaCPU == 1:
    print("Empate!")
elif escolha == 1 and escolhaCPU == 2:
    print("Computador ganhou!")
elif escolha == 2 and escolhaCPU == 0:
    print("Computador ganhou!")
elif escolha == 2 and escolhaCPU == 1:
    print("Você ganhou!")
elif escolha == 2 and escolhaCPU == 2:
    print("Empate!")