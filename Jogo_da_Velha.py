def interface():
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))

def ValidarVitoria(rodada):
    global parar
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro [0][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro [1][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro [2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro [2][0] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True
        
    if(tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro [2][1] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro [2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro [2][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

    if(tabuleiro[2][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro [0][2] == rodada):
        interface()
        print("O jogador {} venceu!".format(rodada))
        parar = True

def PegarJogada():
    jogada_valida = False
    while jogada_valida == False:
        try:
            linha = int (input("Digite a linha escolhida: "))
            coluna = int (input("Digite a coluna escolhida: "))

            if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2 :
                jogada_valida = True

                if tabuleiro[linha][coluna] == " ":
                    jogada_valida = True
                else:
                    jogada_valida = False
                    print("essa posiçao esta ocupada,digite outra linha e coluna vazia")

            else:
             print ("digito errado, digite numeros inteiro de 0 a 2 na linha e na coluna")

        except:
            print("voçe digitou um caractere errado, digite um numero valido")
    return linha, coluna        
    

tabuleiro = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "] ]

parar = False
rodada = "X"
jogadas = 0
while parar == False:
    if jogadas == 9:
        interface()
        print ("Empate!")
        parar = True
    interface()
    print ("SUA VEZ {}".format(rodada))
    linha, coluna = PegarJogada()

    if rodada == "X":
        tabuleiro[linha][coluna] = "X"
        ValidarVitoria(rodada)
        jogadas += 1
        rodada = "O"

    elif rodada == "O":
        tabuleiro[linha][coluna] = "O"
        ValidarVitoria(rodada)
        jogadas += 1
        rodada =  "X"
    


print ("Programa encerrado")

