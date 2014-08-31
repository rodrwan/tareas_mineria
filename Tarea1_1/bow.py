import json
from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup
from tabulate import tabulate
import MontyLemmatiser

DATA_PATH = './data/'
onlyfiles = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
CATEGORIES = {}
with open('categories.json', 'r') as file_:
  results = file_.read()
  CATEGORIES = json.loads(results)

bag_of_words = []
#p = MontyLemmatiser.MontyLemmatiser()
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
          title = title.string.replace("/LOCATION", "").replace("/ORGANIZATION", "").replace("/PERSON", "")
          aux_string = title.split()
          for word in aux_string:
            if word not in bag_of_words:
              bag_of_words.append(word)

        contents = y.findAll('content')
        for content in contents:
          content = content.string.replace("/LOCATION", "").replace("/ORGANIZATION", "").replace("/PERSON", "")
          aux_string = content.split()
          for word in aux_string:
            if word not in bag_of_words:
              bag_of_words.append(word)

        answers = y.findAll('answer')

        for answer in answers:
          answer = answer.string.replace("/LOCATION", "").replace("/ORGANIZATION", "").replace("/PERSON", "")
          aux_string = answer.split()
          for word in aux_string:
            if word not in bag_of_words:
              bag_of_words.append(word)

print len(bag_of_words)
import json
# print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))
with open('bow.json', 'w') as file_:
    file_.write(json.dumps(bag_of_words, sort_keys=True, indent=4, separators=(',', ': ')))