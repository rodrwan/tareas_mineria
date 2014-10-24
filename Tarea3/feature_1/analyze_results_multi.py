#
# undersampling: sacamos tokens
# oversampling: copiamos entidades
#

import json
from os import listdir
from os.path import isfile, join
from load_config import load_config
import random
import os
import sys
from tabulate import tabulate
from sklearn import metrics

if __name__ == "__main__":
  VECTOR_PATH = './folds/splits/test/'
  RESULT_PATH = './folds/results/'

  """
    Load base files with entities, ignored files and categories for this example.
  """
  lc = load_config()
  lc.read_config()
  tokens = lc.get_entities()
  ignored_files = lc.get_ignored()
  CATEGORIES = lc.get_categories()

  files_test = [ VECTOR_PATH+f for f in listdir(VECTOR_PATH) if isfile(join(VECTOR_PATH, f)) and f not in ignored_files ]
  files_result = [ RESULT_PATH+f for f in listdir(RESULT_PATH) if isfile(join(RESULT_PATH, f)) and f not in ignored_files]

  files_test.sort()
  files_result.sort()
  classes_test = []
  _type = sys.argv[1]

  for ft in files_test:
    if 'svm_multi' in ft:
      with open(ft, 'r') as file_:
        content = file_.read()
        content = content.split('\n')
        for samples in content[:-1]:
          samp = samples.split()
          try:
            classes_test.append((samp[0], samp[-2]))
          except:
            print ft
            sys.exit()

  classes_result = []
  for fr in files_result:
    if _type in fr:
      with open(fr, 'r') as file_:
        content = file_.read()
        content = content.split('\n')
        for samples in content[:-1]:
          samp = samples.split()
          classes_result.append((samp[0], samp[-1]))

  accuracies = {}
  accuracy = 0.
  for idx  in range(len(classes_test)):
    if classes_test[idx][1] not in accuracies:
      accuracies[classes_test[idx][1]] = [0, 0]
    else:
      accuracies[classes_test[idx][1]][1] += 1

    if float(classes_test[idx][0]) > 0 and float(classes_result[idx][0]) >= 0:
      accuracies[classes_test[idx][1]][0] += 1

  samples = {}
  y_test_global = []
  probas_global = []
  probas_global_tmp = []
  y_predicted = []
  # 1 entity
  # -1 token
  m_conf = {}
  for idx  in range(len(classes_test)):
    if _type == 'multi':
      y_test_global.append(float(classes_test[idx][0]))
      probas_global.append(float(classes_result[idx][0]))
      probas_global_tmp.append(float(classes_result[idx][0]))
    else:
      probas_global.append(float(classes_result[idx][0]))
      if (float(classes_result[idx][0]) > 0):
        probas_global_tmp.append(1)
      else:
        probas_global_tmp.append(-1)
    if classes_test[idx][1] not in m_conf:
      m_conf[classes_test[idx][1]] = {

        'y_test': [],
        'y_pred': []
      }

    m_conf[classes_test[idx][1]]['y_pred'].append(float(classes_result[idx][0]))
    m_conf[classes_test[idx][1]]['y_test'].append(float(classes_test[idx][0]))
  for mc in m_conf:
    y_test = m_conf[mc]['y_test']
    y_predicted = m_conf[mc]['y_pred']
    print "##########################################################################"
    print "Categoria " + mc.replace('_', ' ') + ":"
    print "##########################################################################"
    print
    print metrics.classification_report(y_test, y_predicted)
    print
    print "Confusion matrix"
    conf_mat = metrics.confusion_matrix(y_test, y_predicted, labels=[1,2,3,4])
    try:
      table = [
        ["Token pred", conf_mat[0][0], conf_mat[0][1], conf_mat[0][2], conf_mat[0][3]],
        ["Organization pred", conf_mat[1][0], conf_mat[1][1], conf_mat[1][2], conf_mat[1][3]],
        ["Location pred", conf_mat[2][0], conf_mat[2][1], conf_mat[2][2], conf_mat[2][3]],
        ["Person pred", conf_mat[3][0], conf_mat[3][1], conf_mat[3][2], conf_mat[3][3]]
      ]
      print tabulate(table, headers=["","Token real", "Organization real", "Location real", "Person real"], tablefmt="grid")
      print
      print
    except:
      sys.exit()
  print metrics.classification_report(y_test_global, probas_global_tmp)
