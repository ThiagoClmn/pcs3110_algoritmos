def binarySearch(vetor, elemento):
	vetor.sort() # pré-requisito: ordenar o vetor
	initialPos = 0
	finalPos = len(vetor) - 1
	while initialPos <= finalPos:
		meio = (initialPos + finalPos)/2
		meio = int(meio)
		if (elemento == vetor[meio]):
			return meio
		elif (elemento < vetor[meio]):
			finalPos = meio
		else:
			initialPos = meio
	return meio

v = [30, 40, 10, 20, 13, 14]

print(binarySearch(v, 20)) # 3
