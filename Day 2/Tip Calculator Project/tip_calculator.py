print("------------------------------------\nBem-vindo a Calculadora de Gorjetas!\n------------------------------------")
conta = float(input("Qual é o valor total da conta?: R$ "))
gorj = int(input("Qual porcentagem de gorjeta você gostaria de contribuir? 10 12 15: "))
pessoas = int(input("Quantas pessoas vão pagar a conta?: "))

total_por_pessoa = (conta + (conta * (gorj / 100))) / pessoas
print(f"O total que cada pessoa deve pagar é R$ `{total_por_pessoa:.2f}`")