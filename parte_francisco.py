def criar_placar():
    return {"X": 0, "O": 0, "empates": 0}


def registrar_resultado(placar, vencedor):
    if vencedor == "X" or vencedor == "O":
        placar[vencedor] += 1
    elif vencedor is None:
        placar["empates"] += 1
    else:
        raise ValueError("O vencedor deve ser 'X', 'O' ou None para empate.")


def limpar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for coluna in range(len(linha)):
            linha[coluna] = " "


def exibir_placar(placar):
    print("===== PLACAR =====")
    print("Jogador X: " + str(placar["X"]))
    print("Jogador O: " + str(placar["O"]))
    print("Empates: " + str(placar["empates"]))


def exibir_estatisticas(placar):
    total_partidas = placar["X"] + placar["O"] + placar["empates"]
    print("===== ESTATISTICAS DA SESSAO =====")
    print("Partidas disputadas: " + str(total_partidas))
    print("Vitorias de X: " + str(placar["X"]))
    print("Vitorias de O: " + str(placar["O"]))
    print("Empates: " + str(placar["empates"]))


def perguntar_revanche():
    while True:
        resposta = input("Jogar novamente? (s/n): ").strip().lower()
        if resposta == "s" or resposta == "sim":
            return True
        if resposta == "n" or resposta == "nao" or resposta == "não":
            return False
        print("Opcao invalida. Digite s para sim ou n para nao.")
