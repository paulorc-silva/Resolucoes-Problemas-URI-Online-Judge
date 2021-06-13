while(True):
	g, p = map(int, input().split())

	if((g == 0) and (p == 0)):
		break

	gp = []

	for i in range(0, g, 1):
		corridas = list(map(int, input().split()))
		gp.append(corridas)

	s = int(input())

	for x in range(0, s, 1):
		pontos = list(map(int, input().split()))
		qtdPontuacao = pontos[0]
		resultado = [0] * p

		for corrida in gp:
			i = 0
			
			for piloto in corrida:
				if(piloto <= qtdPontuacao):
					resultado[i] += pontos[piloto]

				i += 1

		maior = max(resultado)
		empate = resultado.count(maior)

		if(empate == 1):
			print(resultado.index(maior) + 1)
		
		else:
			i = 1
			final = ""
			for maiorResultado in resultado:
				if(maiorResultado == maior):
					final += str(i) + " "
				
				i += 1

			print(final.rstrip(" "))