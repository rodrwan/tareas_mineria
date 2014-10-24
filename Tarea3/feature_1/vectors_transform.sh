#!/bin/sh

TYPE='train'
for idx in {1..10}; do
if [ $idx -eq 10 ]
then
  mallet-2.0.7/mallet-2.0.7/bin/mallet import-svmlight --input ./folds/splits/${TYPE}/${TYPE}_${idx} --output ./folds/splits/${TYPE}/${TYPE}_mallet_${idx}
else
  mallet-2.0.7/mallet-2.0.7/bin/mallet import-svmlight --input ./folds/splits/${TYPE}/${TYPE}_0${idx} --output ./folds/splits/${TYPE}/${TYPE}_mallet_0${idx}
fi
echo "Archivo ${idx} transformado"
done
