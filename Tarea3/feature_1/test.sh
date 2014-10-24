#!/bin/sh

TYPE=$1
for i in {1..10}; do
if [ $i -eq 10 ]
then
  svm_light/svm_classify -v 0 ./folds/splits/test/test_${i} ./folds/models/model_05_${TYPE}_${i} ./folds/results/result_05_${TYPE}_${i}
else
  svm_light/svm_classify -v 0 ./folds/splits/test/test_0${i} ./folds/models/model_05_${TYPE}_0${i} ./folds/results/result_05_${TYPE}_0${i}
fi
echo "Resultado ${i} generado"
done