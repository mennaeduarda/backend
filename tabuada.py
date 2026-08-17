numero = int(input("Digite o número do qual deseja a tabuada: "))
multiplicador = 1

print("Tabuada do", numero)

while multiplicador <= 10:
    resultado = multiplicador * numero
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador += 1