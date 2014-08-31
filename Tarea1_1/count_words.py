import json
from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup
from tabulate import tabulate
import operator

DATA_PATH = './data/'
onlyfiles = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
CATEGORIES = {}
with open('categories.json', 'r') as file_:
  results = file_.read()
  CATEGORIES = json.loads(results)

tokens = 0
words = 0
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
          words += len(title.string.split())

        contents = y.findAll('content')
        for content in contents:
          words += len(content.string.split())

        answers = y.findAll('answer')
        for answer in answers:
          words += len(answer.string.split())

print "Palabras: " + str(words)