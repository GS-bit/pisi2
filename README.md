# PISI2

Projeto desenvolvido para a disciplina de **PISI 2 — Projeto Interdisciplinar de Sistemas de Informação 2**.

# pisi2 — Problema do Caixeiro Viajante (TSP) com Algoritmo Genético

Projeto acadêmico da **UFRPE** que resolve o **TSP (Travelling Salesman Problem)** por meio de um **algoritmo genético**, desenvolvido para a **2ª VA**. Este README descreve a branch `2VA`.

## Sobre o projeto

O Problema do Caixeiro Viajante consiste em encontrar o menor caminho que visita cada cidade exatamente uma vez e retorna à cidade de origem. Como o problema é NP-difícil, o projeto usa uma metaheurística (algoritmo genético, implementado com a biblioteca [PyGAD](https://pygad.readthedocs.io/)) e a avalia em instâncias de vários tamanhos, incluindo a **brazil58**, com 58 cidades do Brasil.

### Configuração do algoritmo genético

| Parâmetro | Valor |
|---|---|
| Tamanho da população (brazil58) | 300 |
| Número de gerações | 3000 |
| Seed | 42 |
| Execuções por instância | 30 |
| Representação | Permutação das cidades (1 a N) |
| Função de aptidão | 1 / custo do ciclo |
| Seleção de pais | Torneio (K = 3), 20 pais por geração |
| Cruzamento | Order Crossover (OX) |
| Mutação | Inversion Mutation (probabilidade de 20% por filho) |
| Elitismo | 2 melhores indivíduos preservados |

## Estrutura do repositório

| Arquivo | Descrição |
|---|---|
| `main.py` | Código principal: lê as instâncias `.tsp` e executa o algoritmo genético |
| `brazil58.tsp` | Instância do TSP com 58 cidades do Brasil |
| `edgesbrasil58.tsp` | Apenas a matriz de distâncias da brazil58 (triangular superior, 57 linhas, sem cabeçalho). Tem os mesmos valores da seção `EDGE_WEIGHT_SECTION` do `brazil58.tsp` e não é lido pelo `main.py` |
| `test10.tsp` – `test13.tsp` | Instâncias menores criadas para testes |
| `.gitignore` | Arquivos ignorados pelo Git |

## Requisitos

- Python 3.x
- `numpy`
- `pygad`

```bash
pip install numpy pygad
```

## Como executar

1. Clone o repositório e acesse a branch `2VA`:

   ```bash
   git clone https://github.com/GS-bit/pisi2.git
   cd pisi2
   git checkout 2VA
   ```

2. Instale as dependências:

   ```bash
   pip install numpy pygad
   ```

3. Execute o programa:

   ```bash
   python main.py
   ```

   A instância é escolhida no próprio `main.py`, pelo nome do arquivo `.tsp` aberto e pelo número de cidades usado na leitura e na população inicial.

## Resultados — brazil58

Foram feitas **30 execuções** com população 300, 3000 gerações e seed 42. Todas as rotas retornadas são válidas (visitam as 58 cidades uma única vez). Como referência, o ótimo conhecido da brazil58 na TSPLIB é **25395**.

| Métrica | Valor |
|---|---|
| Melhor custo | **25395** (execução 14) |
| Pior custo | 28039 (execução 4) |
| Média | 26193,1 |
| Mediana | 25948,5 |
| Desvio padrão | 625,4 |
| Desvio do ótimo (melhor / média / pior) | 0,00% / 3,14% / 10,41% |
| Execuções que atingiram o ótimo | 1 de 30 |
| Execuções a até 1% do ótimo | 4 de 30 |
| Execuções a até 2% do ótimo | 13 de 30 |

**Melhor rota encontrada (execução 14, custo 25395):**

```
[10, 52, 51, 47, 49, 43, 27, 5, 23, 12, 57, 24, 58, 44, 18, 1, 30, 13, 40, 25, 9, 32, 20, 53, 50, 4, 8, 22, 16, 42, 38, 31, 7, 11, 39, 21, 36, 17, 26, 19, 6, 28, 14, 37, 15, 34, 46, 56, 45, 33, 29, 3, 48, 55, 54, 2, 41, 35]
```

O algoritmo atingiu o ótimo conhecido em uma das 30 execuções, e a média ficou cerca de 3% acima dele.

### Instâncias de teste

Os arquivos `test10.tsp` a `test13.tsp` guardam a matriz triangular superior de distâncias (sem diagonal), por isso têm de 11 a 14 cidades. O custo ótimo de cada uma foi calculado de forma exata (programação dinâmica de Held-Karp) e serve de referência para o algoritmo genético.

| Instância | Nº de cidades | Custo ótimo | Rota ótima | Tempo do AG |
|---|---|---|---|---|
| test10 | 11 | 12 | 1, 11, 10, 9, 8, 7, 2, 3, 4, 5, 6 | – |
| test11 | 12 | 14 | 1, 11, 10, 9, 8, 12, 7, 2, 3, 4, 5, 6 | – |
| test12 | 13 | 14 | 1, 11, 10, 9, 8, 13, 12, 7, 2, 3, 4, 5, 6 | – |
| test13 | 14 | 16 | 1, 11, 10, 9, 14, 13, 12, 7, 8, 3, 2, 4, 5, 6 | – |

## Equipe

- [Gabriel Soares](https://github.com/GS-bit)
- [Júlia Carvalho](https://github.com/juliacarvalho12118)
- [DaviDGuarana](https://github.com/DavidGuarana)
- [Eloísa Fe...](https://github.com/efernandapimentel04-dot)

## Licença

Projeto acadêmico, para a disciplina de projeto interdisciplinar de sistema de informação da UFRPE.
