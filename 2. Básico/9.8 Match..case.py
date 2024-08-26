# 5. Match.. case
print("\n5. Match.. case:")
nome = "Maria"
match nome:
    case "Maria":
        print("Olá, Maria!")
    case "João":
        print("Olá, João!")
    case "Ana":
        print("Olá, Ana!")
    case _:
        print("Olá, estranho!")
