"""
Brasil58 - Problema do caixeiro viajante

Alunos:
- Gabriel Soares
- Davi Guaraná
- Eloísa Fernanda
- Júlia Galindo

Período 2026.2

Código desenvolvido a partir de um original fornecido em aula.

*Cada cidade estudada é um inteiro de 1 a 58. 

"""

import random

import numpy as np
import pygad

def custo_caminho(permutacao: list[int], dic_distancias: dict[tuple[int, int], int]) -> int:
	"""
	Função de custo de caminho.
	
	Argumentos:
		permutacao: lista de cidades a serem percorridas sequencialmente (exemplo: [5, 14, 2, 3, 7, ...]).
		dic_distancias: dicionário de distâncias, onde as chaves são tuplas no formato (cidade_inicial, cidade_destino) e seus valores são as distâncias da cidade_inicial à cidade_destino.
	
	Retorno:
		Custo total do caminho.
	"""
	
	soma = 0
	for i in range(len(permutacao)-1):
		a = permutacao[i]
		b = permutacao[i+1]
		if (a,b) in dic_distancias:
			soma += dic_distancias[(a,b)]
		else:
			print(f"Erro! ({a},{b}) não existe no dicionario!")
			exit()
			
	soma += dic_distancias[(permutacao[-1],permutacao[0])]
	
	return soma
	
def inicializar_populacao(tamanho: int, qt_de_cidades: int) -> list[list[int]]:
	"""
	Inicialização da população.
	
	Argumentos:
		tamanho: tamanho da população.
		qt_de_cidades: a quantidade de cidades do problema.
		
	Retorno:
		Uma lista com a população gerada pela função.
	"""
	
	lista = []
	for i in range(tamanho):
		individuo = list(range(1, qt_de_cidades+1))
		random.shuffle(individuo)
		lista.append(individuo)
	return lista

def calcular_aptidao(populacao: list[list[int]], dic_distancias: dict[tuple[int, int], int]) -> list[int]:
	"""
	Cálculo da aptidão.
	
	Argumentos:
		populacao: população a ser analisada.
		dic_distancias: dicionário de distâncias do problema.
	
	Retorno:
		Lista de aptidão.
	"""
	
	lista_aptidao = []
	for elem in populacao:
		lista_aptidao.append(custo_caminho(elem, dic_distancias))
	return lista_aptidao
	
def calcular_resultado(populacao: list[list[int]], dic_distancias: dict[tuple[int, int], int]) -> tuple[list[int], int]:
	"""
	Cálculo do resultado da análise do caixeiro viajante. É usado como operador de cruzamento o Order Crossover e como de mutação o Inversion Mutation.
	
	Argumentos:
		populacao: população inicial.
		dic_distancias: dicionário de distâncias do problema.
		
	Retorno:
		Tupla com a rota final a ser indicada pelo programa (primeira posição) e seu custo (segunda posição).
	"""
	
	if not populacao:
		raise ValueError("A população não pode estar vazia.")

	quantidade_cidades = len(populacao[0])

	if quantidade_cidades < 2:
		raise ValueError("A rota precisa conter pelo menos duas cidades.")

	if any(len(rota) != quantidade_cidades for rota in populacao):
		raise ValueError("Todas as rotas devem ter o mesmo número de cidades.")

	def funcao_aptidao(ga, solucao, indice):
		custo = custo_caminho(
			[int(cidade) for cidade in solucao],
			dic_distancias
		)
		return 1.0 / custo

	def order_crossover(pais, tamanho_filhos, ga):
		filhos = []

		for i in range(tamanho_filhos[0]):
			pai1 = [int(cidade) for cidade in pais[i % len(pais)]]
			pai2 = [int(cidade) for cidade in pais[(i + 1) % len(pais)]]

			inicio, fim = sorted(
				random.sample(range(quantidade_cidades), 2)
			)

			filho = [None] * quantidade_cidades
			filho[inicio:fim + 1] = pai1[inicio:fim + 1]

			genes_restantes = [
				cidade
				for cidade in pai2[fim + 1:] + pai2[:fim + 1]
				if cidade not in filho
			]

			posicoes = (
				list(range(fim + 1, quantidade_cidades))
				+ list(range(0, fim + 1))
			)

			posicoes_livres = [
				posicao for posicao in posicoes
				if filho[posicao] is None
			]

			for posicao, cidade in zip(posicoes_livres, genes_restantes):
				filho[posicao] = cidade

			filhos.append(filho)

		return np.array(filhos, dtype=int)

	def inversion_mutation(filhos, ga):
		for i in range(len(filhos)):
			if random.random() < 0.20:
				inicio, fim = sorted(
					random.sample(range(quantidade_cidades), 2)
				)
				filhos[i, inicio:fim + 1] = (
					filhos[i, inicio:fim + 1][::-1]
				)

		return filhos

	algoritmo = pygad.GA(
		num_generations=500,
		sol_per_pop=len(populacao),
		num_parents_mating=min(20, len(populacao)),
		num_genes=quantidade_cidades,
		gene_type=int,
		gene_space=list(range(1, quantidade_cidades + 1)),
		allow_duplicate_genes=False,
		initial_population=populacao,
		fitness_func=funcao_aptidao,
		parent_selection_type="tournament",
		K_tournament=3,
		keep_elitism=min(2, len(populacao)),
		crossover_type=order_crossover,
		mutation_type=inversion_mutation,
		random_seed=42
	)

	algoritmo.run()

	melhor_solucao, _, _ = algoritmo.best_solution()
	melhor_rota = [int(cidade) for cidade in melhor_solucao]
	melhor_custo = custo_caminho(melhor_rota, dic_distancias)

	return melhor_rota, melhor_custo

def main() -> None:
	"""
	Função principal.
	"""

	objeto_arq = open("test13.tsp")
	
	# Para obter uma lista onde cada objeto será uma string grande representando uma linha do arquivo, descomente isto:
	#lista_linhas = objeto_arq.readlines()  # Cada linha terá um <ENTER> junto com o último elemento.
	
	# Dicionário de distâncias, onde as chaves são tuplas no formato (cidade_inicial, cidade_destino) e seus valores são as distâncias da cidade_inicial à cidade_destino:
	distancias = {}  
	
	for i in range(1, 14): # Será iterado das linhas 1 a 57, pois a 58 não possui aresta.
		linha = objeto_arq.readline() # Lê somente uma linha do arquivo.
		
		# Transformando a linha em lista de strings:
		lista = linha.split()
	
		for j in range(i+1, 15): # Iteração nas colunas i+1 a 58.
			if len(lista) > 0:
				peso = int(lista.pop(0))
			else:
				print(f"Erro! linha {i} do arquivo não possui elementos suficientes")
				exit()
				
			# Gravando a aresta em (i, j) e (j, i):
			distancias[(i,j)] = peso
			distancias[(j,i)] = peso
			
	populacao = inicializar_populacao(100, 14) # População inicial.
	
	resultado = calcular_resultado(populacao, distancias)  # Tupla com a rota final a ser indicada pelo programa (primeira posição) e seu custo (segunda posição).
	
	# Exibição do resultado:
	if resultado:
		print(f"Rota encontrada: {resultado[0]}")
		print(f"Seu custo: {resultado[1]}")
	
	objeto_arq.close()		
		
		
if __name__ == "__main__":
	main()
