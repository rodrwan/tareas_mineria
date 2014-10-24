import random

random.seed(42)
rnd = 0

with open('./all_vectors', 'r') as vects_ , open('./training_bag', 'w') as train_ , open('./test_data', 'w') as test_:
	vectors = vects_.read()
	vectors = vectors.split('\n')
	for v in vectors[:-1]:
		rnd = random.random()
		if rnd < 0.66:
			train_.write(v+'\n')
		else:
			test_.write(v+'\n')

