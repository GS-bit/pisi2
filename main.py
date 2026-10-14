"""
Flyfood - Projeto acadêmico de entrega de comidas via drones

Alunos:
- Gabriel Soares
- Davi Guaraná
- Eloísa Fernanda
- Júlia Galindo

Período 2026.2

"""

from utils import ler_mundo, obter_percurso

def main():
	caminho_mundo = input("Informe a localização do arquivo com os pontos de entrega e o ponto de retorno: ")
	
	mundo = ler_mundo(caminho_mundo)

	if mundo:
		percurso = obter_percurso(mundo)

		if percurso:
			print(f"Rota a ser percorrida: {percurso[0]}")

			print(f"Distância necessária: {percurso[1]}")
		else:
			print("Falha ao obter o percurso do drone!")
	else:
		print("Falha ao ler o arquivo informado!")

if __name__ == '__main__':
	main()
