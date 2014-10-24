#!/bin/bash

C="0.5" #elige tu C favorito

for i in {0..9}; do

	../../svm_light/svm_learn -v 0 -c $C ./training/training_$i ./modelos/model_$i

	echo "Modelo $i generado"

done
