import sys
import json
from os import listdir
from os.path import isfile, join
try:
  from BeautifulSoup import BeautifulSoup
except:
  from bs4 import BeautifulSoup
from tabulate import tabulate
from features import create_main_feature
from load_config import load_config
from log_system import read_log, write_log, clear_log

def clean_word(word,tokens):
  is_token = -1
  for token in tokens:
    if token in word:
      word = word.split('/')[0]
      is_token = 1
      break
  return word, is_token

def generate_bow(qid, bag_of_words, count_bow, word, tokens, text):
  word, token = clean_word(word, tokens)
  tmp_bow_f1 = create_main_feature(qid, word, token, text, tokens)
  index = 0
  is_there = False
  for idx in bag_of_words:
    if bag_of_words[idx]['features_1'] == tmp_bow_f1:
      is_there = True
      index = idx
      break
    else:
      index += 1
  if is_there:
    bag_of_words[index]['cuenta'] += 1
  else:
    bag_of_words[count_bow] = {}
    bag_of_words[count_bow]['features_1'] = {}
    bag_of_words[count_bow]['features_1'] = tmp_bow_f1
    bag_of_words[count_bow]['cuenta'] = 1
    count_bow += 1
  del tmp_bow_f1
  return bag_of_words, count_bow

"""
  Main part of the program
"""
if __name__ == "__main__":
  DATA_PATH = './data/'
  files = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]

  lc = load_config()
  lc.read_config()
  tokens = lc.get_entities()
  ignored_files = lc.get_ignored()
  CATEGORIES = lc.get_categories()

  try:
    files = [f for f in files if f not in ignored_files]
    lfile = read_log()
    if lfile == '':
      lidx = 0
    else:
      lidx = files.index(lfile)

    files = files[lidx:]
    for _file in files:
      bag_of_words = {}
      bag_of_keys = {}
      key_id = 0
      count_bow = 0
      cat_count = 1
      if (CATEGORIES[_file][1] == "Done"):
        category = CATEGORIES[_file][0]
        print "##################################"
        print "Category: " + category
        file_name = DATA_PATH + _file
        f = open(file_name, 'r')
        content = f.read()
        y = BeautifulSoup(content)
        questions = y.findAll('question')
        for question in questions:
          qid = question['id']
          y = BeautifulSoup(str(question))
          titles = y.findAll('title')
          for title in titles:
            stitle = title.string.split()
            for st in stitle:
              bag_of_words, count_bow = generate_bow(qid, bag_of_words, count_bow, st, tokens, title.string)

          contents = y.findAll('content')
          for content in contents:
            scontent = content.string.split()
            for sc in scontent:
              bag_of_words, count_bow = generate_bow(qid, bag_of_words, count_bow, sc, tokens, content.string)

          answers = y.findAll('answer')
          for answer in answers:
            sanswer = answer.string.split()
            for sa in sanswer:
              bag_of_words, count_bow = generate_bow(qid, bag_of_words, count_bow, sa, tokens, answer.string)
        for bow in bag_of_words:
          for key in bag_of_words[bow]['features_1'].keys():
            if key not in bag_of_keys and 'ES_TOKEN' not in key and 'qid' not in key:
              bag_of_keys[key] = key_id
              key_id+=1

        with open('json_data/'+str(_file)+'-key.json', 'w') as file_:
          file_.write(json.dumps(bag_of_keys, sort_keys=True, indent=4, separators=(',', ': ')))
        print "Hash con llaves escrito: "+category
        with open('json_data/'+str(_file)+'.json', 'w') as file_:
          file_.write(json.dumps(bag_of_words, sort_keys=True, indent=4, separators=(',', ': ')))
        print "se escribio: "+category
        cat_count += 1
        print
    print "All the jobs was done!"
    clear_log()
  except (KeyboardInterrupt, SystemExit):
    print "The system has stopped"
    write_log(_file)