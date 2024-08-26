professor = input("Digite o nome do professor: ")
materia = input("""Digite o número correspondente a matéria do professor:
                    1. Matemática
                    2. Física
                    3. Química
                    4. Biologia
                    5. Python\n\n""")

var1 = "Conteúdo de matemática"
var2 = "Conteúdo de física"
var3 = "Conteúdo de química"
var4 = "Conteúdo de biologia"
var5 = "Conteúdo de python"


# Desenvolva uma aplicação que retorne o conteúdo correspondente do professor conforme o número
# da matéria

# Início do fluxo de verificação do conteúdo do professor
if materia == "1":
    print(f"O conteúdo do professor {professor} é {var1}")

elif materia == "2":
    print(f"O conteúdo do professor {professor} é {var2}")

elif materia == "3":
    print(f"O conteúdo do professor {professor} é {var3}")

elif materia == "4":
    print(f"O conteúdo do professor {professor} é {var4}")

elif materia == "5":
    print(f"O conteúdo do professor {professor} é {var5}")

else:
    print(f"Conteúdo não encontrado para o professor {professor}")

