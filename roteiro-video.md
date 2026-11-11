# Roteiro de apresentação — Jogo da Velha

**Duração sugerida:** 3 a 4 minutos  
**Formato:** gravação de tela do terminal com a fala dos integrantes

## 1. Abertura — Marlon (20 segundos)

> “Este é o nosso Jogo da Velha, feito em Python para dois jogadores e executado no terminal. O repositório e o README mostram como executar o programa.”

Mostrar o menu principal e escolher **Ver regras**; voltar ao menu e iniciar uma partida.

## 2. Tabuleiro e validações — Marlon (45 a 60 segundos)

Explicar que `tabuleiro` é uma matriz de três linhas por três colunas e que os `for` percorrem suas posições para exibi-las. Mostrar as identificações de linhas e colunas.

Demonstrar três entradas inválidas, por exemplo:

1. Digitar uma opção inexistente no menu.
2. Informar uma linha fora do intervalo de 1 a 3.
3. Tentar jogar em uma casa já ocupada.

Explicar que o programa pede outra entrada e informa o erro.

## 3. Regras da partida — Pedro (60 a 75 segundos)

Demonstrar uma vitória de X e apontar a linha completada. Explicar que os jogadores alternam símbolos e que os laços `for` contam as marcas nas linhas e colunas; outro `for` verifica as diagonais. Mostrar a mensagem de vitória.

Iniciar outra partida e demonstrar um empate com o tabuleiro cheio. Explicar que o programa verifica vitória antes de declarar empate.

As sequências usadas para estas duas demonstrações estão registradas em `evidencias/vitoria.txt` e `evidencias/empate.txt`.

## 4. Placar e revanche — Francisco (45 a 60 segundos)

Mostrar o resultado acumulado depois da partida e a opção de revanche. Escolher jogar novamente e mostrar que a nova partida começa com o tabuleiro limpo. Depois, escolher não jogar novamente e mostrar a opção de consultar o placar no menu.

Por fim, escolher **Sair** e mostrar as estatísticas da sessão (partidas disputadas, vitórias de X e de O, empates). Explicar que o total é a soma dos três contadores do placar e que, sem nenhuma partida, o programa avisa que nada foi disputado. A sequência completa dessa demonstração está registrada em `evidencias/sessao.txt`.

O desafio de série melhor de 3/5 **não** foi implementado; não apresentá-lo como função pronta. Se o grupo decidir realizá-lo, atualizar este roteiro para incluir a demonstração.

## 5. Encerramento — Francisco (10 a 15 segundos)

> “O código, as instruções de execução e a divisão das tarefas estão no repositório. Obrigado por assistir.”

## Checklist de gravação

- [ ] Abrir `main.py` a partir da pasta do projeto.
- [ ] Gravar em uma janela legível e manter o tabuleiro visível durante as jogadas.
- [ ] Cada integrante explica sua própria parte.
- [ ] Mostrar as três entradas inválidas, uma vitória, um empate, o placar, a revanche e as estatísticas ao sair.
- [ ] Salvar o vídeo final na pasta compartilhada do grupo.
