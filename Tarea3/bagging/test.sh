#!/bin/sh

for i in {0..9}; do

	../../svm_light/svm_classify -v 0 test_data ./modelos/model_${i} ./resultados_ind/result_m${i}

	echo "Resultado ${i} generado"

done
