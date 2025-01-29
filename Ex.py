perguntas = [
    {
        "Pergunta" : "Quanto é 2+2?",
        "Opções" : ["1", "2", "3", "4"],
        "Resposta" : "4",
    },
    {
        "Pergunta" : "Quanto é 5*5?",
        "Opções" : ["25", "55", "10", "51"],
        "Resposta" : "25",
    },
    {
        "Pergunta" : "Quanto é 10/2",
        "Opções" : ["4", "5", "2", "1"],
        "Resposta" : "5",          
    }
]
acertos = 0
num = 0

for pergunta in perguntas:
    num = 0
    print("")
    print(pergunta["Pergunta"])
    for opcao in pergunta["Opções"]:
        print(f"{num}) {opcao}")
        num += 1
        if num == 4:
            print("")
            resp = input("Digite sua resposta: ")
            if resp == pergunta["Resposta"]:
                print("")
                print("Resposta certa!")
                acertos += 1
            else:
                print("")
                print("Errado!")

print("")
print(f"Sua pontuação foi de: {acertos} de 3")