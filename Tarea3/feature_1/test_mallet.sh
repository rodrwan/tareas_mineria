#!/bin/sh

TYPE=$1
for i in {1..10}; do
if [ $i -eq 10 ]
then
  ./mallet-2.0.7/mallet-2.0.7/bin/mallet classify-file --input ./folds/splits/test/test_${i} --output ./folds/results/result_${TYPE}_${i} --classifier ./folds/models/model_${TYPE}_${i}
else
  ./mallet-2.0.7/mallet-2.0.7/bin/mallet classify-file --input ./folds/splits/test/test_0${i} --output ./folds/results/result_${TYPE}_0${i} --classifier ./folds/models/model_${TYPE}_0${i}
fi
echo "Resultado ${i} generado"
done