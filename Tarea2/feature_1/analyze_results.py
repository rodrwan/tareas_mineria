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

  classes_test = []
  for ft in files_test:
    with open(ft, 'r') as file_:
      content = file_.read()
      content = content.split('\n')
      for samples in content[:-1]:
        samp = samples.split()
        classes_test.append((samp[0], samp[-2]))

  classes_result = []
  for fr in files_result:
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
    probas_global.append(float(classes_result[idx][0]))
    if (float(classes_result[idx][0]) > 0):
      probas_global_tmp.append(1)
    else:
      probas_global_tmp.append(-1)
    if classes_test[idx][1] not in m_conf:
      m_conf[classes_test[idx][1]] = {
        'real_entity': 0,
        'real_token': 0,
        'total_examples': 0,
        'y_test': [],
        'y_pred': []
      }

    if int(classes_test[idx][0]) == 1:
      m_conf[classes_test[idx][1]]['real_entity'] += 1
      y_test_global.append(1)
    else:
      m_conf[classes_test[idx][1]]['real_token'] += 1
      y_test_global.append(-1)

    if float(classes_result[idx][0]) < 0:
      m_conf[classes_test[idx][1]]['y_pred'].append(-1)
    else:
      m_conf[classes_test[idx][1]]['y_pred'].append(1)
    m_conf[classes_test[idx][1]]['y_test'].append(int(classes_test[idx][0]))
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
    conf_mat = metrics.confusion_matrix(y_test, y_predicted)
    table = [
      ["Entity pred", conf_mat[1][1], conf_mat[1][0]],
      ["Token pred", conf_mat[0][1], conf_mat[0][0]]
    ]
    print tabulate(table, headers=["","Entity real", "Token real"], tablefmt="grid")
    print
    print

  print metrics.classification_report(y_test_global, probas_global_tmp)
  import pylab as pl
  from sklearn.metrics import roc_curve, auc
  # Compute ROC curve and area the curve
  fpr, tpr, thresholds = roc_curve(y_test_global, probas_global)
  roc_auc = auc(fpr, tpr)
  print "Area under the ROC curve : %f" % roc_auc
  # Plot ROC curve
  pl.clf()
  pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
  pl.plot([0, 1], [0, 1], 'k--')
  pl.xlim([0.0, 1.0])
  pl.ylim([0.0, 1.0])
  pl.xlabel('False Positive Rate')
  pl.ylabel('True Positive Rate')
  pl.title('ROC para primer grupo de features')
  pl.legend(loc="lower right")
  pl.show()