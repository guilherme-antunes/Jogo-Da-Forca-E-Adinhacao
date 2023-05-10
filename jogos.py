import forca
import adivinhacao

def escolhe_jogo():
    print("***********************")
    print("***Escolha seu jogo!***")
    print("***********************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo você quer jogar?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    if(jogo != 1 or 2 or str):
        escolhe_jogo()


if(__name__ == "__main__"):
     escolhe_jogo()