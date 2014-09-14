#!/bin/sh

for i in {1..10}; do
if [ $i -eq 10 ]
then
  ./svm_light/svm_learn -v 0 -c 1.0 ./folds/splits/train/train_${i} ./folds/models/model_${i}
else
  ./svm_light/svm_learn -v 0 -c 1.0 ./folds/splits/train/train_0${i} ./folds/models/model_0$i
fi
echo "Modelo ${i} generado"
done