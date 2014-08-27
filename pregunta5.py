import json
from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup
from tabulate import tabulate
import MontyTagger

DATA_PATH = './data/'
onlyfiles = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
CATEGORIES = {}
with open('categories.json', 'r') as file_:
  results = file_.read()
  CATEGORIES = json.loads(results)

m=MontyTagger.MontyTagger(0)
loc, org, per = 0.0, 0.0, 0.0

dictionary = {}
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
          tokens = []
          for word in stitle:
            if '/ORGANIZATION' in word:
              pass
            elif '/LOCATION' in word:
              pass
            elif '/PERSON' in word:
              pass
            else:
              tokens.append(word)
          title = " ".join(tokens)
          title = m.tag(title, 0, 0)
          stitle = title.split(" ")
          for word in stitle:
            if len(word.encode('utf-8').split("/")) > 0:
              cat = word.encode('utf-8').split("/")[1]
              if cat not in dictionary:
                dictionary[cat] = 1
              else:
                dictionary[cat] +=1

        contents = y.findAll('content')
        for content in contents:
          content = content.string
          scontent = content.split()
          tokens = []
          for word in scontent:
            if '/ORGANIZATION' in word:
              pass
            elif '/LOCATION' in word:
              pass
            elif '/PERSON' in word:
              pass
            else:
              tokens.append(word)
          content = " ".join(tokens)
          content = m.tag(content, 0, 0)
          scontent = content.split(" ")
          for word in scontent:
            if len(word.encode('utf-8').split("/")) > 0:
              cat = word.encode('utf-8').split("/")[1]
              if cat not in dictionary:
                dictionary[cat] = 1
              else:
                dictionary[cat] +=1

        answers = y.findAll('answer')
        for answer in answers:
          answer = answer.string
          sanswer = answer.split()
          tokens = []
          for word in sanswer:
            if '/ORGANIZATION' in word:
              pass
            elif '/LOCATION' in word:
              pass
            elif '/PERSON' in word:
              pass
            else:
              tokens.append(word)
          answer = " ".join(tokens)
          answer = m.tag(answer, 0, 0)
          sanswer = answer.split(" ")
          for word in sanswer:
            if len(word.encode('utf-8').split("/")) > 1:
              cat = word.encode('utf-8').split("/")[1]
              if cat not in dictionary:
                dictionary[cat] = 1
              else:
                dictionary[cat] +=1
print
dictionary.pop('``', None)
dictionary.pop(':', None)
dictionary.pop(')', None)
dictionary.pop('(', None)
dictionary.pop('\'\'', None)
dictionary.pop('#', None)
dictionary.pop(',', None)
dictionary.pop('.', None)
dictionary.pop('$', None)
# print dictionary
import json
# print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))
with open('sintactic_categories.json', 'w') as file_:
    file_.write(json.dumps(dictionary, sort_keys=True, indent=4, separators=(',', ': ')))