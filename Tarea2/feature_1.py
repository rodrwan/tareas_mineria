import json
from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup
from tabulate import tabulate
from features import create_main_feature

def clean_word(word,tokens):
  is_token = -1
  for token in tokens:
    if token in word:
      word = word.split('/')[0]
      is_token = 1
      break
  return word, is_token

def generate_bow(bag_of_words, count_bow, word, tokens):
  word, token = clean_word(word, tokens)
  tmp_bow_f1 = create_main_feature(word, token)
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
  onlyfiles = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
  CATEGORIES = {}
  with open('categories.json', 'r') as file_:
    results = file_.read()
    CATEGORIES = json.loads(results)

  bag_of_words = {}
  bag_of_keys = {}
  key_id = 0
  count_bow = 0
  cat_count = 1
  tokens = ['/ORGANIZATION', '/LOCATION', '/PERSON']
  for _file in onlyfiles:
    if _file != '.DS_Store':
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
          y = BeautifulSoup(str(question))
          titles = y.findAll('title')
          for title in titles:
            stitle = title.string.split()
            for st in stitle:
              bag_of_words, count_bow = generate_bow(bag_of_words, count_bow, st, tokens)

          contents = y.findAll('content')
          for content in contents:
            scontent = content.string.split()
            for sc in scontent:
              bag_of_words, count_bow = generate_bow(bag_of_words, count_bow, sc, tokens)

          answers = y.findAll('answer')
          for answer in answers:
            sanswer = answer.string.split()
            for sa in sanswer:
              bag_of_words, count_bow = generate_bow(bag_of_words, count_bow, sa, tokens)
        for bow in bag_of_words:
          for key in bag_of_words[bow]['features_1'].keys():
            if key not in bag_of_keys:
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
  # print " ".join(newString).encode('utf-8')