response = ""
idade = int(input("Digite a idade do aluno: "))

if idade >= 18:
    response = "Aluno é de maior"
else:
    response = "Aluno é de menor"

# print(response)

resposta = "Aluno é de maior" if idade >= 18 else "Aluno é de menor"
print(resposta)