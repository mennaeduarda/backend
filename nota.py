while True:
    nota = float(input("Digite a nota do aluno: "))

    if nota >= 0 and nota <= 10:
        print("Nota computada.")
    else:
        print("Nota inválida.")
        break
