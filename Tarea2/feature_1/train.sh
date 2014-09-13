#!/bin/sh

svm_light/svm_learn -c 1.0 folds/splits/train/train_01 folds/models/model_01
svm_light/svm_learn -c 1.0 folds/splits/train/train_02 folds/models/model_02
svm_light/svm_learn -c 1.0 folds/splits/train/train_03 folds/models/model_03
svm_light/svm_learn -c 1.0 folds/splits/train/train_04 folds/models/model_04
svm_light/svm_learn -c 1.0 folds/splits/train/train_05 folds/models/model_05
svm_light/svm_learn -c 1.0 folds/splits/train/train_06 folds/models/model_06
svm_light/svm_learn -c 1.0 folds/splits/train/train_07 folds/models/model_07
svm_light/svm_learn -c 1.0 folds/splits/train/train_08 folds/models/model_08
svm_light/svm_learn -c 1.0 folds/splits/train/train_09 folds/models/model_09
svm_light/svm_learn -c 1.0 folds/splits/train/train_10 folds/models/model_10
