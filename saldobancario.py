saldo = float(input("Digite seu saldo inicial:" ))

while saldo > 0:
    saque = float(input("Digite a quantia que deseja sacar: "))
    saldo = saldo - saque
    print("Seu saldo é: ", saldo)

if saldo == 0:
    print("Seu saldo se encontra zerado.")