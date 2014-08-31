import json
from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup
from tabulate import tabulate
from utils import is_capitalized, full_upper, full_lower, has_root, sin_cat, word_len

def clean_word(word):
  if '/ORGANIZATION' in word:
    word = word.split('/')[0]
  elif '/LOCATION' in word:
    word = word.split('/')[0]
  elif '/PERSON' in word:
    word = word.split('/')[0]
  return word

def create_feature(word):
  tmp_bow = {}
  tmp_bow['TIENE_RAIZ'] = has_root(word)
  tmp_bow['FULL_MAYUSCULAS'] = full_upper(word)
  tmp_bow['FULL_MINUSCULAS'] = full_lower(word)
  tmp_bow['INICIO__MAYUSCULAS_RESTO_MINUSCULAS'] = is_capitalized(word)
  tmp_bow['CAT_SINTACTICA_'+ sin_cat(word)] = 1
  tmp_bow['PALABRA_'+word] = 1
  tmp_bow['PALABRA_LARGO'] = word_len(word)
  return tmp_bow

def generate_bow(bag_of_words, count_bow, word):
  word = clean_word(word)
  bag_of_words[count_bow] = {}
  bag_of_words[count_bow]['features'] = {}
  tmp_bow = create_feature(word)
  index = 0
  is_there = False
  for idx in bag_of_words:
    if bag_of_words[idx]['features'] == tmp_bow:
      is_there = True
      index = idx
      break
    else:
      index += 1
  if is_there:
    bag_of_words[index]['cuenta'] += 1
  else:
    bag_of_words[count_bow]['features'] = tmp_bow
    bag_of_words[count_bow]['cuenta'] = 1
    count_bow += 1
  del tmp_bow
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
  count_bow = 0
  cat_count = 1
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
        loc, org, per = 0, 0, 0
        lem_loc, lem_org, lem_per = 0, 0, 0
        for question in questions:
          y = BeautifulSoup(str(question))
          titles = y.findAll('title')
          for title in titles:
            stitle = title.string.split()
            for st in stitle:
              bag_of_words, count_bow = generate_bow(bag_of_words, count_bow, st)

          contents = y.findAll('content')
          for content in contents:
            scontent = content.string.split()
            for sc in scontent:
              bag_of_words, count_bow = generate_bow(bag_of_words, count_bow, sc)

          answers = y.findAll('answer')
          for answer in answers:
            sanswer = answer.string.split()
            for sa in sanswer:
              bag_of_words, count_bow = generate_bow(bag_of_words, count_bow, sa)

        with open('category_'+str(cat_count)+'json', 'w') as file_:
          file_.write(json.dumps(bag_of_words, sort_keys=True, indent=4, separators=(',', ': ')))
        print "se escribio category_"+str(cat_count)
        cat_count += 1
        print

  print "All the jobs was done!"
  # print " ".join(newString).encode('utf-8')