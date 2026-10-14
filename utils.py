from itertools import permutations

import time

def ler_mundo(arquivo: str) -> list:
    """
    Lê um arquivo contendo as coordenadas dos pontos de entrega de comida e do ponto de retorno do drone.

    O conteúdo do arquivo segue este formato matricial:

    i j
    a11 a12 ... a1j
    a21 a22 ... a2j
    ... ... ... ...
    ai1 ai2 ... aij

    i e j são, respectivamente, os números de linhas e colunas da matriz;
    axy, em que 1 <= x <= i e 1 <= y <= j, deve assumir um dos seguintes valores:
        - 0, que é um ponto padrão
        - R, que é o ponto de retorno do drone
        - A, B, C, D, E, F... (menos o R), que são os pontos de entrega

    Parâmetros:
        arquivo: caminho do arquivo no computador.

    Retorno:
        Uma lista de tuplas que representam pontos e que seguem o formato (nome, x, y), 
        em que nome indica o rótulo do ponto, seja ele de retorno (R) ou de entrega (A, B, C, D, E, F... menos o R), 
        x é o valor inteiro da coordenada horizontal do ponto e y o da coordenada vertical.

        E, em caso de erro na leitura do arquivo, uma lista vazia.
    """
    pontos = []

    try:
        with open(arquivo, "r") as f:
            linhas = f.readlines()

            if len(linhas) > 0:
                cabecalho = linhas[0]
                partes = cabecalho.split()
                i = int(partes[0])
                j = int(partes[1])

                for linha_i in range(1, i+1):
                    linha_matriz = linhas[linha_i]
                    separador = linha_matriz.split()

                    for separador_i, valor in enumerate(separador):
                        x = linha_i-1
                        y = separador_i

                        if valor != "0":
                            ponto = (valor, x, y)
                            pontos.append(ponto)
                            
                return pontos

            else:
                return []

    except Exception:
        return []

def obter_percurso(mundo: list) -> tuple:
    """
    Obtém o menor percurso que o drone deve realizar para entregar as comidas.

    Parâmetros:
        mundo: uma lista de tuplas que representam pontos e que seguem o formato (nome, x, y), 
        em que nome indica o rótulo do ponto, seja ele de retorno (R) ou de entrega (A, B, C, D, E, F... menos o R), 
        x é o valor inteiro da coordenada horizontal do ponto e y o da coordenada vertical.

    Retorno:
        Uma tupla cujo primeiro elemento é uma string (por exemplo, "A D C B") que indica a sequência de pontos 
	a ser percorrida pelo drone e cujo segundo elemento é a distância desse percurso.

        E, em caso de erro na execução da função, uma string vazia.
    """
    
    try:
        origem = None
        entregas = []

        for ponto in mundo:
            nome, x, y = ponto

            if nome == "R":
                origem = ponto
            else:
                entregas.append(ponto)

        if origem is None:
            return ""

        if len(entregas) == 0:
            return ""

        menor_distancia = float("inf")
        melhor_percurso = None

        inicio_tempo = time.time()

        for percurso in permutations(entregas):

            distancia_total = 0
            ponto_atual = origem

            for ponto in percurso:
                distancia_total += (
                    abs(ponto_atual[1] - ponto[1])
                    + abs(ponto_atual[2] - ponto[2])
                )

                ponto_atual = ponto

            distancia_total += (
                abs(ponto_atual[1] - origem[1])
                + abs(ponto_atual[2] - origem[2])
            )

            if distancia_total < menor_distancia:
                menor_distancia = distancia_total
                melhor_percurso = percurso

        print(f"Algoritmo executado com sucesso em {round(time.time() - inicio_tempo, 2)}s")

        resultado = (" ".join(ponto[0] for ponto in melhor_percurso), menor_distancia)

        return resultado

    except Exception:
        return ""
