import random

random.seed(43*43)	#because of reasons
rnd = 0
acc = 0

with open('./training_bag', 'r') as train_:
	train_data = train_.read()
	train_data = train_data.split('\n')
	if train_data[-1] == "":
		train_data.pop(-1)		#una linea vacia me estaba jodiendo
						
	for i in range(10):
		with open('./training/training_'+str(i), 'w') as td:
			for t in range(len(train_data)):
				rnd = random.randint(0,len(train_data)-1)
				td.write(train_data[rnd])
				if t < len(train_data)-1:
					td.write('\n')
		print "training_"+str(i)+" listo."
	
