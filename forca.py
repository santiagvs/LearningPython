def jogar():
    print("*********************************")
    print("***Bem vindo no jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                print(f"Encontrei a letra {letra} na posição {index}")
            index += 1
        print("jogando")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
