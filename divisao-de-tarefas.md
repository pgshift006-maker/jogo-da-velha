# Divisão de tarefas — Jogo da Velha

**Integrantes:** Pedro, Marlon e Francisco  
**Projeto:** jogo da velha em Python, executado no terminal.  
**Repositório GitHub:** [pgshift006-maker/jogo-da-velha](https://github.com/pgshift006-maker/jogo-da-velha)

## Divisão das responsabilidades

| Parte | Responsável | Afazeres |
|---|---|---|
| Base e entradas | **Marlon** | Preparar a matriz 3×3; exibir o tabuleiro com `for` aninhado e identificação das linhas e colunas; criar o menu com `while` e a tela de regras; validar as entradas e impedir jogadas em casas ocupadas. |
| Regras da partida | **Pedro** | Alternar os símbolos `X` e `O`; controlar o laço da partida; verificar vitória em linhas, colunas e diagonais com `for`; detectar empate quando o tabuleiro estiver cheio. |
| Placar e desafios | **Francisco** | Manter o placar acumulado; limpar a matriz entre partidas; permitir jogar novamente; implementar, se der tempo, série de melhor de 3 ou 5 e estatísticas da sessão ao sair. |

> A série de melhor de 3 ou 5 e as estatísticas da sessão são desafios extras. A prioridade é entregar o jogo completo com as regras principais funcionando.

## GitHub

- **Pedro:** criar o repositório e adicionar como colaboradores Marlon (`@wizzy-glitch`) e Francisco (`@fconeto03`). O professor `@profmartinz` também foi convidado porque o repositório é privado.
- **Pedro:** revisar o código dos colegas e conferir se o projeto atende às restrições do item 3 do trabalho.
- **Francisco:** escrever e atualizar o `README.md` com a descrição e as instruções para executar o jogo.

Cada integrante deve fazer seus próprios commits, na própria conta e computador. A orientação da atividade pede pelo menos **5 commits ao longo de 3 dias diferentes** para cada integrante.

### Fluxo de trabalho para evitar conflitos

A branch `main` deve guardar a versão integrada e estável. Cada pessoa desenvolve em uma branch própria:

- **Marlon:** `marlon-tabuleiro`
- **Pedro:** `pedro-regras`
- **Francisco:** `francisco-placar`

Cada integrante clona o repositório no próprio computador, cria sua branch e trabalha nela. Exemplo para Pedro:

```bash
git clone https://github.com/pgshift006-maker/jogo-da-velha.git
cd jogo-da-velha
git switch -c pedro-regras
# fazer uma parte do trabalho
git add .
git commit -m "Adiciona verificacao de vitoria"
git push -u origin pedro-regras
```

Marlon e Francisco usam os mesmos comandos, trocando `pedro-regras` pelos nomes de suas branches. Cada um deve usar sua própria conta do GitHub e fazer commits de mudanças reais. A meta da atividade é pelo menos **5 commits em 3 dias diferentes por integrante**.

Quando a branch estiver pronta, o integrante abre um **Pull Request** para `main`. Pedro revisa o código e integra os Pull Requests um por vez. Ao fazer o merge, escolham **Create a merge commit** para manter os commits de cada pessoa no histórico; não usem *squash*.

Como as partes do jogo estão no mesmo arquivo, `main.py`, combinem quem edita cada seção e evitem alterar as mesmas linhas ao mesmo tempo. Esperem a integração de um Pull Request antes de atualizar a branch seguinte. Para trazer as atualizações de `main` para uma branch já publicada, usem:

```bash
git switch nome-da-sua-branch
git pull origin main
git push
```

Se o Git indicar conflito, parem para revisar as partes marcadas no arquivo, preservem a lógica correta, salvem e concluam o merge antes de continuar. Não apaguem mudanças de outra pessoa sem combinar com ela.

## Relatório

- **Marlon:** identificação dos integrantes, link do repositório, explicação das variáveis e da matriz, e descrição do uso de `while`.
- **Pedro:** teste de mesa de um `for` aninhado; explicação dos operadores e das estruturas `if`/`elif`/`else`.
- **Francisco:** tabela de testes, desafios implementados e localização deles no código; registro da divisão de tarefas.

## Vídeo de apresentação

- **Marlon:** demonstrar o jogo e três entradas inválidas; explicar a matriz e a exibição do tabuleiro.
- **Pedro:** demonstrar uma vitória e um empate; explicar a verificação dos resultados com `for`.
- **Francisco:** demonstrar os desafios e o placar; explicar essa parte do código e editar o vídeo.

## Cronograma de commits — sugestão

A foto mostra o início do cronograma em **01/11**, **02/11** e **03/11**; as últimas linhas estão parcialmente encobertas. Esta sugestão distribui as tarefas principais sem atribuir como transcrição os trechos que não estão legíveis.

| Data | Marlon | Pedro | Francisco |
|---|---|---|---|
| **Dom, 01/11** | Criar o projeto e o README inicial; preparar e exibir a matriz 3×3. | Planejar e iniciar a lógica das regras da partida. | Preparar a estrutura inicial das variáveis do placar. |
| **Seg, 02/11** | Implementar o menu principal e a validação das entradas. | Implementar a alternância entre `X` e `O`. | Iniciar o placar acumulado e a limpeza do tabuleiro. |
| **Ter, 03/11** | Completar a validação de linha e coluna e revisar a exibição. | Implementar as verificações de vitória e empate. | Implementar jogar novamente e avançar nos desafios extras. |

## Checklist de entrega

- [ ] Jogo permite iniciar partida, ver regras e sair pelo menu.
- [ ] Entradas inválidas e casas ocupadas são tratadas.
- [ ] Jogadores alternam entre `X` e `O`.
- [ ] Vitória e empate são detectados corretamente.
- [ ] Placar funciona e o tabuleiro é reiniciado entre partidas.
- [ ] Repositório, README, relatório e vídeo estão prontos.
- [ ] Desafios extras foram feitos se houver tempo.





