import time
contagem = int(input("Digite um número para começar sua contagem regressiva: "))

while contagem > 0:
    print(contagem)
    time.sleep(1)
    contagem -= 1

print("Sua contagem chegou ao fim.")