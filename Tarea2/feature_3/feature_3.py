import sys
import json
from os import listdir
from os.path import isfile, join
try:
  from BeautifulSoup import BeautifulSoup
except:
  from bs4 import BeautifulSoup
from tabulate import tabulate
from features import create_third_feature
from load_config import load_config
from log_system import read_log, write_log, clear_log
import MontyLingua.MontyTagger
m = MontyLingua.MontyTagger.MontyTagger(0)

reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

def clean_word(stext, entities):
  is_token = -1
  enti = 'TOKEN'
  for entity in entities:
    if entity in stext:
      enti = stext.split('/')[1]
      stext = stext.split('/')[0]
      is_token = 1
      break
  return stext, is_token, enti

def clean_text(text, entities):
  for entity in entities:
    text = text.replace(entity, '').replace(' -RRB- ', ' ').replace(' -LRB- ', ' ').replace('\/', '#').replace(' -RRB-', '').replace('-LRB- ', '')
  return text

def generate_bow(qid, bag_of_words, count_bow, word, tokens, text, word_id, tags, ori_text):
  for stext in ori_text.split():
    sword, is_token, _entity = clean_word(stext, entities)
    if word == sword:
      break
  tmp_bow_f1 = create_third_feature(qid, word, text, tokens, word_id, tags, is_token)
  tmp_bow_f1['ENTITY'] = _entity
  # print json.dumps(tmp_bow_f1, sort_keys=True, indent=4, separators=(',', ': '))
  # sys.exit()
  index = 0
  is_there = False
  for idx in bag_of_words:
    if bag_of_words[idx]['features'] == tmp_bow_f1:
      is_there = True
      index = idx
      break
    else:
      index += 1
  if is_there:
    bag_of_words[index]['cuenta'] += 1
  else:
    bag_of_words[count_bow] = {}
    bag_of_words[count_bow]['features'] = {}
    bag_of_words[count_bow]['features'] = tmp_bow_f1
    bag_of_words[count_bow]['cuenta'] = 1
    count_bow += 1
  del tmp_bow_f1
  return bag_of_words, count_bow

"""
  Main part of the program
"""
if __name__ == "__main__":
  DATA_PATH = '../data/'
  files = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]

  lc = load_config()
  lc.read_config()
  entities = lc.get_entities()
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
    bag_of_keys = {}
    key_id = 1
    for _file in files:
      bag_of_words = {}
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
            if title.string:
              text = clean_text(title.string, entities)
              stitle = text.split()
              word_id = 0
              text = "@#@# @#@# @#@# " + text + " @#@# @#@# @#@#".encode('utf-8')
              tags = m.tag_tokenized(text, 0, 0)
              stop = len(stitle)
              for st in stitle:
                bag_of_words, count_bow = generate_bow(qid, bag_of_words, count_bow, st, entities, text, word_id+3, tags, title.string)
                word_id+=1

          contents = y.findAll('content')
          for content in contents:
            if content.string:
              text = clean_text(content.string, entities)
              scontent = text.split()
              word_id = 0
              text = "@#@# @#@# @#@# " + text + " @#@# @#@# @#@#".encode('utf-8')
              tags = m.tag_tokenized(text, 0, 0)
              stop = len(scontent)
              for sc in scontent:
                bag_of_words, count_bow = generate_bow(qid, bag_of_words, count_bow, sc, entities, text, word_id+3, tags, content.string)
                word_id+=1

          answers = y.findAll('answer')
          for answer in answers:
            if answer.string:
              text = clean_text(answer.string, entities)
              sanswer = text.split()
              word_id = 0
              text = "@#@# @#@# @#@# " + text + " @#@# @#@# @#@#".encode('utf-8')
              tags = m.tag_tokenized(text, 0, 0)
              stop = len(sanswer)
              try:
                for sa in sanswer:
                  bag_of_words, count_bow = generate_bow(qid, bag_of_words, count_bow, sa, entities, text, word_id+3, tags, answer.string)
                  word_id+=1
              except:
                print sanswer
                print
                print text
                print word_id
                print len(sanswer)
                print "Cago la wea"
                sys.exit()

        for bow in bag_of_words:
          for key in bag_of_words[bow]['features'].keys():
            if key not in bag_of_keys and 'ES_TOKEN' not in key and 'qid' not in key and 'PALABRA' not in key:
              bag_of_keys[key.encode('utf-8')] = key_id
              key_id+=1

        file_ = codecs.open('json_data/'+str(_file)+'.json', 'w', "utf-8")
        # with open('json_data/'+str(_file)+'.json', 'w') as file_:
        file_.write(json.dumps(bag_of_words, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False).encode('utf8'))
        file_.close()
        print "se escribio: "+category
        cat_count += 1
        print
    file_ = codecs.open('json_data/hash-key.json', 'w', "utf-8")
    # with open('json_data/'+str(_file)+'-key.json', 'w') as file_:
    file_.write(json.dumps(bag_of_keys, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False).encode('utf8'))
    file_.close()
    print "Hash con llaves escrito: "+category
    print "All the jobs was done!"
    clear_log()
  except (KeyboardInterrupt, SystemExit):
    print "The system has stopped"
    write_log(_file)