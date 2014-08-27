import json
from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup
from tabulate import tabulate
import math

def log2(x):
  return math.log(x, 2)

DATA_PATH = './data/'
onlyfiles = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
CATEGORIES = {}
with open('categories.json', 'r') as file_:
  results = file_.read()
  CATEGORIES = json.loads(results)

total, is_entity, is_suggest = 0.0, 0.0, 0.0
is_not_entity = 0.0
org_sugges, loc_sugges, per_sugges = 0.0, 0.0, 0.0
org_real, loc_real, per_real = 0.0, 0.0, 0.0
tokens = 0.0
entities = 0.0
total_word = 0.0
p_org, p_loc, p_per = 0.0, 0.0, 0.0
for _file in onlyfiles:
  if _file != '.DS_Store':
    if (CATEGORIES[_file][1] == "Done"):
      category = CATEGORIES[_file][0]
      file_name = DATA_PATH + _file
      f = open(file_name, 'r')
      content = f.read()
      y = BeautifulSoup(content)
      questions = y.findAll('question')
      for question in questions:
        y = BeautifulSoup(str(question))
        suggestions = y.findAll('suggestions')
        j = 0
        titles = y.findAll('title')
        for title in titles:
          total_word += len(title.string.split())
          suggestion = suggestions[j].string
          j+=1
          if suggestion != None:
            sugges_split = suggestion.split()
            aux_string = title.string.split()
            total+=len(sugges_split)
            for sugges in sugges_split:
              for word in aux_string:
                if '/ORGANIZATION' in word:
                  words = word.split('/ORGANIZATION')
                  word = words[0].lower() + '/ORGANIZATION'
                elif '/LOCATION' in word:
                  words = word.split('/LOCATION')
                  word = words[0].lower() + '/LOCATION'
                elif '/PERSON' in word:
                  words = word.split('/PERSON')
                  word = words[0].lower() + '/PERSON'
                if sugges in word:
                  is_entity+=1.
                  is_suggest+=1.
              if '/ORGANIZATION' in sugges:
                is_not_entity+=1.
              elif '/LOCATION' in sugges:
                is_not_entity+=1.
              elif '/PERSON' in sugges:
                is_not_entity+=1.


          for word in title.string.split():
            if '/ORGANIZATION' in word:
              org_real+=1.
            elif '/LOCATION' in word:
              loc_real+=1.
            elif '/PERSON' in word:
              per_real+=1.
            else:
              tokens+=1.

        contents = y.findAll('content')
        for content in contents:
          total_word += len(content.string.split())
          suggestion = suggestions[j].string
          j+=1
          if suggestion != None:
            sugges_split = suggestion.split()
            aux_string = content.string.split()
            total+=len(sugges_split)
            for sugges in sugges_split:
              for word in aux_string:
                if '/ORGANIZATION' in word:
                  words = word.split('/ORGANIZATION')
                  word = words[0].lower() + '/ORGANIZATION'
                elif '/LOCATION' in word:
                  words = word.split('/LOCATION')
                  word = words[0].lower() + '/LOCATION'
                elif '/PERSON' in word:
                  words = word.split('/PERSON')
                  word = words[0].lower() + '/PERSON'
                if sugges in word:
                  is_entity+=1.
                  is_suggest+=1.
              if '/ORGANIZATION' in sugges:
                is_not_entity+=1.
              elif '/LOCATION' in sugges:
                is_not_entity+=1.
              elif '/PERSON' in sugges:
                is_not_entity+=1.

          for word in content.string.split():
            if '/ORGANIZATION' in word:
              org_real+=1.
            elif '/LOCATION' in word:
              loc_real+=1.
            elif '/PERSON' in word:
              per_real+=1.
            else:
              tokens+=1.

        answers = y.findAll('answer')
        for answer in answers:
          total_word += len(answer.string.split())
          suggestion = suggestions[j].string
          j+=1
          if suggestion != None:
            sugges_split = suggestion.split()
            aux_string = answer.string.split()
            total+=len(sugges_split)
            for sugges in sugges_split:
              for word in aux_string:
                if '/ORGANIZATION' in word:
                  words = word.split('/ORGANIZATION')
                  word = words[0].lower() + '/ORGANIZATION'
                elif '/LOCATION' in word:
                  words = word.split('/LOCATION')
                  word = words[0].lower() + '/LOCATION'
                elif '/PERSON' in word:
                  words = word.split('/PERSON')
                  word = words[0].lower() + '/PERSON'
                if sugges in word:
                  is_entity+=1.
                  is_suggest+=1.
              if '/ORGANIZATION' in sugges:
                is_not_entity+=1.
              elif '/LOCATION' in sugges:
                is_not_entity+=1.
              elif '/PERSON' in sugges:
                is_not_entity+=1.

          for word in answer.string.split():
            if '/ORGANIZATION' in word:
              org_real+=1.
            elif '/LOCATION' in word:
              loc_real+=1.
            elif '/PERSON' in word:
              per_real+=1.
            else:
              tokens+=1.

entities += org_real+loc_real+per_real

print

is_not_entity = is_not_entity-is_entity

accuracy = float(is_entity/total)
precision = float((is_entity-is_not_entity)/is_suggest)
recall = float((is_entity-is_not_entity)/entities)

print "Accuracy: {0:.2f}".format(accuracy)
print "Precision: {0:.2f}".format(precision)
print "Recall: {0:.2f}".format(recall)
print "F-Score: {0:.2f}".format(2*((precision*recall)/(precision+recall)))
print
print "Entidades totales: {0:.0f}".format(entities)
print "Tokens totales: {0:.0f}".format(tokens)
print "Palabras totales: {0:.0f}".format(total_word)

p_ent = entities/total_word
p_tok = tokens/total_word
entro = -p_ent*log2(p_ent)-p_tok*log2(p_tok)
print "Entropia: {0:.2f}".format(entro)
print
