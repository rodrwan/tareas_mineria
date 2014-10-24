import random
import sys

random.seed(42)
rnd = 0
results_list = []
progresive_votelist = []
desempate = []

for i in range(10):
	with open('./resultados_ind/result_m'+str(i), 'r') as res_ :
		result = res_.read()
		result = result.split('\n')
		if result[-1] == "":
			result.pop(-1)
		results_list.append(result)

# inicializar lista de votos con el resultado 0
for v in results_list[0]:
	if float(v) >= 0:
		progresive_votelist.append(1)
	else:
		progresive_votelist.append(-1)
	desempate.append(v)

# en total, vamos a escribir 9 resultados combinados
for j in range(1,10):
	with open('./resultados_colectivos/result_vote_0to'+str(j), 'w') as res_c :
		for k in range(len(results_list[j])):
			if float(results_list[j][k]) >= 0:
				progresive_votelist[k] += 1
			else:
				progresive_votelist[k] -= 1
			if abs(float(results_list[j][k])) > abs(float(desempate[k])):
				desempate[k] = results_list[j][k]
			if progresive_votelist[k] == 0:
				res_c.write(desempate[k]+'\n')
			else :
				res_c.write(str(progresive_votelist[k])+'\n')

# No se si se me sigue la idea, la votelist solo mantiene un recuento de
# votos, sumando +1 y -1 segun corresponda. Solo cuando esta lista sea 0
# para un vector determinado, habra un empate, que se resuelve con el
# desempate (valor mas pesado hasta el momento).
# Como nuestro problema es solo la clasificacion binaria, no nos importa
# que los resultados tengan numeros de valor hasta +10/-10, pues solo
# importa si son mayor o menor que 0.
# Ademas, esto permite detectar los empates, ya que son los unicos con
# cifras decimales en los resultados


