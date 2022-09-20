arestas = [
  [1],#0
  [0,2],#1
  [1,3,4],#2
  [2,4,5],#3
  [2,3,5],#4
  [3,4,6],#5
  [5,7,8],#6
  [6],#7
  [6],#8
]

inicial = 2
visitados = []

visitados = [False] * len(arestas)

def busca(verticeAtual, distancia):
  visitados[verticeAtual] = distancia

  for i in range(0, len(arestas[verticeAtual]), 1):
    vizinho = arestas[verticeAtual][i]

    if visitados[vizinho] is False:
      busca(vizinho, distancia + 1)

busca(inicial, 0)

print ("Resultado:")
for i in range (0, len(visitados), 1):
    print("[", i, "] -> ", visitados[i])