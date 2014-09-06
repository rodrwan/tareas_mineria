import json
from os import listdir
from os.path import isfile, join
from load_config import load_config
import random
import os
import sys

if __name__ == "__main__":
  VECTOR_PATH = './folds/splits/test/'
  RESULT_PATH = './folds/results/'

  files = [ f for f in listdir(VECTOR_PATH) if isfile(join(VECTOR_PATH, f)) ]
  """
    Load base files with entities, ignored files and categories for this example.
  """
  lc = load_config()
  lc.read_config()
  tokens = lc.get_entities()
  ignored_files = lc.get_ignored()
  CATEGORIES = lc.get_categories()
  # files = [DATA_PATH+f for f in files if f not in ignored_files]

  print files