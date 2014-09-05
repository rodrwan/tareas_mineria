import json
from os import listdir
from os.path import isfile, join
from load_config import load_config
import random
import os
import sys

if __name__ == "__main__":
  DATA_PATH = './vectors/'
  FOLD_PATH = './folds/'
  files = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
  """
    Load base files with entities, ignored files and categories for this example.
  """
  lc = load_config()
  lc.read_config()
  tokens = lc.get_entities()
  ignored_files = lc.get_ignored()
  CATEGORIES = lc.get_categories()
  # files = [DATA_PATH+f for f in files if f not in ignored_files]

  # Primero debemos agrupar los vectores por qid y ademas por categoria.
  questions_by_cat = []
  for category in CATEGORIES:
    questions = {}
    _file = DATA_PATH + category + '-vec.txt'
    with open(_file, 'r') as file_:
      results = file_.read()
      vectors = results.split('\n')
      del vectors[-1]
      for vector in vectors:
        info = vector.split('#')[1].strip()
        qid = info.split()[0]
        if qid not in questions:
          questions[qid] = []
        else:
          questions[qid].append(vector)
      questions_by_cat.append(questions)

  # Luego extraemos el 10% de los qids con sus respectivos vectores.
  split_percentage = 0.1
  splits = 10
  array_samp = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

  idx = int(sys.argv[1])
  test = []
  train = []
  for i in range(len(questions_by_cat)-1):
    ini = array_samp[idx]
    fin = ini+3
    for question in questions_by_cat[i]:
      if i >= ini and i < fin:
        test += questions_by_cat[i][question]
      else:
        train += questions_by_cat[i][question]

  # Por cada una de las categorias agregamos esos vectores al split.
  # Luego creamos los folds
  newpathtest = FOLD_PATH+'splits/test/'

  if not os.path.exists(newpathtest): os.makedirs(newpathtest)
  end_file = open(newpathtest+'test_'+str(idx+1)+'.txt', 'a')
  for s in test:
    end_file.write(s+'\n')
  end_file.close()

  newpathtrain = FOLD_PATH+'splits/train/'

  if not os.path.exists(newpathtrain): os.makedirs(newpathtrain)
  end_file = open(newpathtrain+'train_'+str(idx+1)+'.txt', 'a')
  for s in train:
    end_file.write(s+'\n')
  end_file.close()

