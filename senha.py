senha_correta = 1234
tentativas = 3

while tentativas > 0:
    senha = int(input("Digite sua senha: "))

    if senha == senha_correta:
        print("Senha correta, seja bem vindo, Admin!")
        break #Interrompe o loop!!

    else:
        tentativas -= 1
        print("Senha incorreta, você tem mais ", tentativas, "tentativas")

if tentativas == 0:
    print("Acesso negado, você esgotou suas tentativas.")