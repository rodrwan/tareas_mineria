import json
from os import listdir
from os.path import isfile, join
from load_config import load_config
import random
import os
import sys
from tabulate import tabulate


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
        classes_test.append((samp[0], samp[-1]))

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

  # print json.dumps(accuracies, sort_keys=True, indent=4, separators=(',', ': '))

  print "Accuracy por categoria: "
  for category in accuracies:
    num = float(accuracies[category][0])
    den = float(accuracies[category][1])
    acc = float(num/den)
    print category + ': ' + str(acc)

  print
  print "Matriz de confusion: "
  tp = 0
  fp = 0
  fn = 0
  tn = 0
  samples = {}
  # 1 entity
  # -1 token
  m_conf = {}
  for idx  in range(len(classes_test)):
    if classes_test[idx][1] not in m_conf:
      m_conf[classes_test[idx][1]] = {
        'tp': 0,
        'fp': 0,
        'fn': 0,
        'tn': 0
      }

    # result is 1 and test is 1
    if float(classes_result[idx][0]) > 0 and int(classes_test[idx][0]) == 1:
      m_conf[classes_test[idx][1]]['tp'] += 1
    # result is 1 but test is -1
    if float(classes_result[idx][0]) > 0 and int(classes_test[idx][0]) == -1:
      m_conf[classes_test[idx][1]]['fp'] += 1
    # result is -1 but test is 1
    if float(classes_result[idx][0]) < 0 and int(classes_test[idx][0]) == 1:
      m_conf[classes_test[idx][1]]['fn'] += 1
    # result is -1 but test is -1
    if float(classes_result[idx][0]) < 0 and int(classes_test[idx][0]) == -1:
      m_conf[classes_test[idx][1]]['tn'] += 1

  for mc in m_conf:
    print "Categoria " + mc.replace('_', ' ') + ":"
    table = [
      ["Entity pred", m_conf[mc]['tp'], m_conf[mc]['fp']],
      ["Token pred", m_conf[mc]['fn'], m_conf[mc]['tn']]
    ]
    print tabulate(table, headers=["","Entity real", "Token real"], tablefmt="grid")
    print







