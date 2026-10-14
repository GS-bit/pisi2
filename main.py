"""
Flyfood - Projeto acadêmico de entrega de comidas via drones

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
	
def calcular_resultado(populacao: list[list[int]]) -> tuple[list[int], int]:
	"""
	Cálculo do resultado da análise do caixeiro viajante.
	
	Argumentos:
		populacao: população inicial.
		
	Retorno:
		Tupla com a rota final a ser indicada pelo programa (primeira posição) e seu custo (segunda posição).
	"""
	
	pass

def main() -> None:
	"""
	Função principal.
	"""

	objeto_arq = open("edgesbrasil58.tsp")
	
	# Para obter uma lista onde cada objeto será uma string grande representando uma linha do arquivo, descomente isto:
	#lista_linhas = objeto_arq.readlines()  # Cada linha terá um <ENTER> junto com o último elemento.
	
	# Dicionário de distâncias, onde as chaves são tuplas no formato (cidade_inicial, cidade_destino) e seus valores são as distâncias da cidade_inicial à cidade_destino:
	distancias = {}  
	
	for i in range(1, 58): # Será iterado das linhas 1 a 57, pois a 58 não possui aresta.
		linha = objeto_arq.readline() # Lê somente uma linha do arquivo.
		
		# Transformando a linha em lista de strings:
		lista = linha.split()
	
		for j in range(i+1, 59): # Iteração nas colunas i+1 a 58.
			if len(lista) > 0:
				peso = int(lista.pop(0))
			else:
				print(f"Erro! linha {i} do arquivo não possui elementos suficientes")
				exit()
				
			# Gravando a aresta em (i, j) e (j, i):
			distancias[(i,j)] = peso
			distancias[(j,i)] = peso
			
	populacao = inicializar_populacao(100, 58) # População inicial.
	
	resultado = calcular_resultado(populacao)  # Tupla com a rota final a ser indicada pelo programa (primeira posição) e seu custo (segunda posição).
	
	# Exibição do resultado:
	if resultado:
		print(f"Rota encontrada: {resultado[0]}")
		print(f"Seu custo: {resultado[1]}")
	
	objeto_arq.close()		
		
		
if __name__ == "__main__":
	main()
