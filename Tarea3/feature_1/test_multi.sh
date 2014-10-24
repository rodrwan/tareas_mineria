#!/bin/sh

TYPE=$1
for i in {1..10}; do
if [ $i -eq 10 ]
then
  ./svm_multiclass/svm_multiclass_classify -v 0 ./folds/splits/test/test_${TYPE}_${i} ./folds/models/model_${TYPE}_${i} ./folds/results/result_${TYPE}_${i}
else
  ./svm_multiclass/svm_multiclass_classify -v 0 ./folds/splits/test/test_${TYPE}_0${i} ./folds/models/model_${TYPE}_0${i} ./folds/results/result_${TYPE}_0${i}
fi
echo "Resultado ${i} generado"
done