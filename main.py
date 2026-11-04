# Jogo da Velha no terminal
# Trabalho da 2a Avaliacao - Coding - Prof. Tiago Martins Ribeiro

# ==================== SECAO 1: VARIAVEIS E MATRIZ (Marlon) ====================
# O tabuleiro e uma matriz 3x3: tabuleiro[i][j], em que i e a linha e j a coluna
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

simbolo = "X"          # simbolo de quem joga agora
jogadas = 0            # quantas casas ja foram marcadas no tabuleiro
programa_ativo = True  # controla o menu principal

# ==================== SECAO 2: VARIAVEIS DO PLACAR (Francisco) ====================

# ==================== SECAO 3: MENU PRINCIPAL (Marlon) ====================
# Este while mantem o menu aberto ate o jogador escolher Sair
while programa_ativo == True:
    print()
    print("===== JOGO DA VELHA =====")
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")

    # Repete a leitura ate a opcao ser valida
    opcao_valida = False
    while opcao_valida == False:
        entrada = input("Escolha uma opcao (1 a 4): ")
        # Compara o texto digitado com cada opcao: "1", "2", "3" e "4"
        for n in range(1, 5):
            if entrada == str(n):
                opcao_valida = True
                opcao = n
        if opcao_valida == False:
            # Mostra o que foi digitado para o jogador perceber o erro
            if entrada == "":
                print("Opcao invalida! Voce nao digitou nada. Digite um numero de 1 a 4.")
            else:
                print("Opcao invalida! Voce digitou '" + entrada + "'. Digite um numero de 1 a 4.")

    if opcao == 1:
        # ==================== SECAO 4: PARTIDA ====================
        # TEMPORARIO: o PG troca esta condicao pela verificacao de
        # vitoria e empate, e o Francisco zera "jogadas" ao limpar o tabuleiro
        while jogadas < 9:
            # Exibicao do tabuleiro (Marlon)
            print()
            print("         1   2   3   (colunas)")
            # O for de fora percorre as linhas da matriz
            for i in range(3):
                texto_linha = "Linha " + str(i + 1) + " "
                # O for de dentro percorre as colunas da linha i
                for j in range(3):
                    texto_linha = texto_linha + " " + tabuleiro[i][j] + " "
                    if j < 2:
                        texto_linha = texto_linha + "|"
                print(texto_linha)
                if i < 2:
                    print("        ---+---+---")
            print()

            print("Vez do jogador " + simbolo)

            # Leitura da jogada com validacao (Marlon)
            # Este while repete a jogada inteira se a casa estiver ocupada
            casa_livre = False
            while casa_livre == False:
                # Repete a leitura ate a linha ser valida
                linha_valida = False
                while linha_valida == False:
                    entrada = input("Escolha a linha (1 a 3): ")
                    # Compara o texto digitado com "1", "2" e "3"
                    for n in range(1, 4):
                        if entrada == str(n):
                            linha_valida = True
                            linha = n - 1  # indice da matriz (0 a 2)
                    if linha_valida == False:
                        if entrada == "":
                            print("Entrada invalida! Voce nao digitou nada. Digite um numero de 1 a 3.")
                        else:
                            print("Entrada invalida! Voce digitou '" + entrada + "'. Digite um numero de 1 a 3.")
                    else:
                        # Confere se a linha escolhida ainda tem alguma casa vazia
                        casas_vazias = 0
                        for j in range(3):
                            if tabuleiro[linha][j] == " ":
                                casas_vazias = casas_vazias + 1
                        if casas_vazias == 0:
                            print("A linha " + str(linha + 1) + " esta cheia! Escolha outra linha.")
                            linha_valida = False

                # Repete a leitura ate a coluna ser valida
                coluna_valida = False
                while coluna_valida == False:
                    entrada = input("Escolha a coluna (1 a 3): ")
                    # Compara o texto digitado com "1", "2" e "3"
                    for n in range(1, 4):
                        if entrada == str(n):
                            coluna_valida = True
                            coluna = n - 1  # indice da matriz (0 a 2)
                    if coluna_valida == False:
                        if entrada == "":
                            print("Entrada invalida! Voce nao digitou nada. Digite um numero de 1 a 3.")
                        else:
                            print("Entrada invalida! Voce digitou '" + entrada + "'. Digite um numero de 1 a 3.")

                # So aceita a jogada se a casa escolhida estiver vazia
                if tabuleiro[linha][coluna] == " ":
                    casa_livre = True
                else:
                    # Informa qual casa foi escolhida e quem ja marcou nela
                    print("Casa ocupada! A linha " + str(linha + 1) + ", coluna " + str(coluna + 1) + " ja esta marcada com " + tabuleiro[linha][coluna] + ". Escolha outra jogada.")

            tabuleiro[linha][coluna] = simbolo
            jogadas = jogadas + 1

            # Verificacao de vitoria e empate e troca de jogador (PG)

        # Exibe o tabuleiro final da partida
        print()
        print("         1   2   3   (colunas)")
        # Mesmos lacos da exibicao: linhas por fora, colunas por dentro
        for i in range(3):
            texto_linha = "Linha " + str(i + 1) + " "
            for j in range(3):
                texto_linha = texto_linha + " " + tabuleiro[i][j] + " "
                if j < 2:
                    texto_linha = texto_linha + "|"
            print(texto_linha)
            if i < 2:
                print("        ---+---+---")
        print()
        print("Fim da partida.")

        # Resultado, placar, serie e jogar novamente (Francisco)

    elif opcao == 2:
        print()
        print("===== REGRAS =====")
        print("Dois jogadores se alternam marcando X e O em casas vazias.")
        print("Para jogar, informe a linha e a coluna da casa desejada.")
        print("Vence quem completar uma linha, uma coluna ou uma diagonal.")
        print("Se o tabuleiro encher sem vencedor, a partida termina empatada.")

    elif opcao == 3:
        # Exibicao do placar (Francisco)
        print("Placar ainda nao disponivel.")

    else:
        # Estatisticas da sessao ao sair (Francisco)
        print("Ate a proxima!")
        programa_ativo = False
