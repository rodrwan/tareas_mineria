#!/bin/sh

TYPE=$1
C="0.5"
for i in {1..10}; do
if [ $i -eq 10 ]
then
  ./svm_light/svm_learn -v 0 -c $C ./folds/splits/train/train_${TYPE}_${i} ./folds/models/model_05_${TYPE}_${i}
else
  ./svm_light/svm_learn -v 0 -c $C ./folds/splits/train/train_${TYPE}_0${i} ./folds/models/model_05_${TYPE}_0$i
fi
echo "Modelo ${i} generado"
done