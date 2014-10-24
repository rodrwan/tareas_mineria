#!/bin/sh

TYPE=$1
for i in {1..10}; do
if [ $i -eq 10 ]
then
  ./mallet-2.0.7/mallet-2.0.7/bin/mallet train-classifier --input ./folds/splits/train/train_mallet_${i} --output-classifier ./folds/models/model_bayes_$i #--trainer MaxEnt
else
  ./mallet-2.0.7/mallet-2.0.7/bin/mallet train-classifier --input ./folds/splits/train/train_mallet_0${i} --output-classifier ./folds/models/model_bayes_0$i #--trainer MaxEnt
fi
echo "Modelo ${i} generado"
done