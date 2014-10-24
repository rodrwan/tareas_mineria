#!/bin/sh

TYPE="svm_multi"
for i in {1..10}; do
if [ $i -eq 10 ]
then
  ./svm_multiclass/svm_multiclass_learn -v 0 -c 1.0 ./folds/splits/train/train_${TYPE}_${i} ./folds/models/model_${TYPE}_${i}
else
  ./svm_multiclass/svm_multiclass_learn -v 0 -c 1.0 ./folds/splits/train/train_${TYPE}_0${i} ./folds/models/model_${TYPE}_0$i
fi
echo "Modelo ${i} generado"
done