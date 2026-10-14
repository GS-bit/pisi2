# FlyFlood

Projeto desenvolvido para a disciplina de **PISI 2 — Projeto Interdisciplinar de Sistemas de Informação 2**.

## 📋 Sobre o Projeto

O FlyFlood é um sistema que calcula a rota mais eficiente para um drone realizar entregas em uma cidade representada por uma matriz. O drone parte de um ponto de referência (R), visita todos os pontos de entrega e retorna ao ponto de origem, sempre se movimentando apenas na horizontal ou na vertical.

## ⚙️ Como funciona

### Leitura do mundo
A função `ler_mundo(arquivo)` é responsável por interpretar o arquivo de texto que descreve a matriz da cidade e transformá-lo em uma lista de pontos utilizável pelo restante do programa:
- Abre o arquivo e lê a primeira linha;
- Percorre cada uma das linhas seguintes da matriz;
- Verifica o valor de cada célula;
- Devolve uma lista com todas as tuplas de pontos encontrados;
- Trata erros para que o programa não trave caso algo dê errado.

### Cálculo da melhor rota
A função `obter_percurso` é responsável por calcular a melhor rota do drone e segue os seguintes passos:
1. Separa o ponto de referência (R) dos pontos de entrega;
2. Gera todas as possíveis ordens de visita utilizando `permutations`;
3. Para cada ordem, calcula o custo do percurso usando a **distância de Manhattan**, já que o drone só pode se mover horizontal ou verticalmente;
4. O percurso sempre começa em R, passa por todas as entregas e retorna a R;
5. A cada percurso calculado, compara a distância obtida com a menor distância encontrada até o momento;
6. Ao final, retorna apenas os nomes dos pontos na ordem do melhor percurso, separados por espaços.

## 👥 Integrantes e Responsabilidades

| Integrante | Responsabilidade |
|---|---|
| Julia | `ler_mundo` |
| Davi Guarana | `obter_percurso` (cálculo da melhor rota) |
| Eloísa Fernanda | README e relatório final |
| Gabriel | Organização e distribuição das tarefas entre os integrantes |

## 📄 Licença

Projeto acadêmico desenvolvido para fins educacionais.
