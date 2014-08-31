import json
from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup
from tabulate import tabulate
import MontyTagger
import operator

DATA_PATH = './data/'
onlyfiles = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
CATEGORIES = {}
with open('categories.json', 'r') as file_:
  results = file_.read()
  CATEGORIES = json.loads(results)

m=MontyTagger.MontyTagger(0)
loc, org, per = 0.0, 0.0, 0.0
dictionary_org = {}
dictionary_loc = {}
dictionary_per = {}
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
        titles = y.findAll('title')
        for title in titles:
          title = title.string
          stitle = title.split()
          index = 0
          for word in stitle:
            if '/ORGANIZATION' in word:
              tword = m.tag(stitle[index-1], 0, 0)
              cat = tword.encode('utf-8').split("/")[1]
              if cat not in dictionary_org:
                dictionary_org[cat] = 1
              else:
                dictionary_org[cat] +=1
            elif '/LOCATION' in word:
              tword = m.tag(stitle[index-1], 0, 0)
              cat = tword.encode('utf-8').split("/")[1]
              if cat not in dictionary_loc:
                dictionary_loc[cat] = 1
              else:
                dictionary_loc[cat] +=1
            elif '/PERSON' in word:
              tword = m.tag(stitle[index-1], 0, 0)
              cat = tword.encode('utf-8').split("/")[1]
              if cat not in dictionary_per:
                dictionary_per[cat] = 1
              else:
                dictionary_per[cat] +=1
            index+=1
        contents = y.findAll('content')
        for content in contents:
          content = content.string
          scontent = content.split()
          index = 0
          for word in scontent:
            if '/ORGANIZATION' in word:
              try:
                tword = m.tag(scontent[index-1], 0, 0)
                cat = tword.encode('utf-8').split("/")[1]
                if cat not in dictionary_org:
                  dictionary_org[cat] = 1
                else:
                  dictionary_org[cat] +=1
              except:
                pass
            elif '/LOCATION' in word:
              try:
                tword = m.tag(scontent[index-1], 0, 0)
                cat = tword.encode('utf-8').split("/")[1]
                if cat not in dictionary_loc:
                  dictionary_loc[cat] = 1
                else:
                  dictionary_loc[cat] +=1
              except:
                pass
            elif '/PERSON' in word:
              try:
                tword = m.tag(scontent[index-1], 0, 0)
                cat = tword.encode('utf-8').split("/")[1]
                if cat not in dictionary_per:
                  dictionary_per[cat] = 1
                else:
                  dictionary_per[cat] +=1
              except:
                pass
            index+=1
        answers = y.findAll('answer')
        for answer in answers:
          answer = answer.string
          sanswer = answer.split()
          index = 0
          for word in sanswer:
            if '/ORGANIZATION' in word:
              try:
                tword = m.tag(sanswer[index-1], 0, 0)
                cat = tword.encode('utf-8').split("/")[1]
                if cat not in dictionary_org:
                  dictionary_org[cat] = 1
                else:
                  dictionary_org[cat] +=1
              except:
                pass
            elif '/LOCATION' in word:
              try:
                tword = m.tag(sanswer[index-1], 0, 0)
                cat = tword.encode('utf-8').split("/")[1]
                if cat not in dictionary_loc:
                  dictionary_loc[cat] = 1
                else:
                  dictionary_loc[cat] +=1
              except:
                pass
            elif '/PERSON' in word:
              try:
                tword = m.tag(sanswer[index-1], 0, 0)
                cat = tword.encode('utf-8').split("/")[1]
                if cat not in dictionary_per:
                  dictionary_per[cat] = 1
                else:
                  dictionary_per[cat] +=1
              except:
                pass
            index+=1

dictionary_org.pop('``', None)
dictionary_org.pop(':', None)
dictionary_org.pop(')', None)
dictionary_org.pop('(', None)
dictionary_org.pop('\'\'', None)
dictionary_org.pop('#', None)
dictionary_org.pop(',', None)
dictionary_org.pop('.', None)
dictionary_org.pop('$', None)
sorted_sc_org = sorted(dictionary_org.iteritems(), key=operator.itemgetter(1), reverse=True)

table = []
j = 0
for i in sorted_sc_org:
  table.append([i[0], i[1]])
  j+=1
  if j == 5: break
print
print "Organization: "
print tabulate(table, headers=["Categoria Sintactica", "Cuenta"], tablefmt="orgtbl")
print

dictionary_loc.pop('``', None)
dictionary_loc.pop(':', None)
dictionary_loc.pop(')', None)
dictionary_loc.pop('(', None)
dictionary_loc.pop('\'\'', None)
dictionary_loc.pop('#', None)
dictionary_loc.pop(',', None)
dictionary_loc.pop('.', None)
dictionary_loc.pop('$', None)
sorted_sc_loc = sorted(dictionary_loc.iteritems(), key=operator.itemgetter(1), reverse=True)

table = []
j = 0
for i in sorted_sc_loc:
  table.append([i[0], i[1]])
  j+=1
  if j == 5: break
print
print "Location: "
print tabulate(table, headers=["Categoria Sintactica", "Cuenta"], tablefmt="orgtbl")
print

dictionary_per.pop('``', None)
dictionary_per.pop(':', None)
dictionary_per.pop(')', None)
dictionary_per.pop('(', None)
dictionary_per.pop('\'\'', None)
dictionary_per.pop('#', None)
dictionary_per.pop(',', None)
dictionary_per.pop('.', None)
dictionary_per.pop('$', None)
sorted_sc_per = sorted(dictionary_per.iteritems(), key=operator.itemgetter(1), reverse=True)

table = []
j = 0
for i in sorted_sc_per:
  table.append([i[0], i[1]])
  j+=1
  if j == 5: break
print
print "Person: "
print tabulate(table, headers=["Categoria Sintactica", "Cuenta"], tablefmt="orgtbl")
print