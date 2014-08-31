import json
from os import listdir
from os.path import isfile, join
from BeautifulSoup import BeautifulSoup
from tabulate import tabulate

DATA_PATH = './data/'
onlyfiles = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
CATEGORIES = {}
with open('categories.json', 'r') as file_:
  results = file_.read()
  CATEGORIES = json.loads(results)

bag_of_words = []
total = 0
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
          aux_string = title.split()
          for word in aux_string:
            if word not in bag_of_words:
              bag_of_words.append(word)

        contents = y.findAll('content')
        for content in contents:
          content = content.string
          aux_string = content.split()
          for word in aux_string:
            if word not in bag_of_words:
              bag_of_words.append(word)

        answers = y.findAll('answer')
        for answer in answers:
          answer = answer.string
          aux_string = answer.split()
          for word in aux_string:
            if word not in bag_of_words:
              bag_of_words.append(word)

loc, org, per, tok, nor = 0, 0, 0, 0, 0
for word in bag_of_words:
  if '/LOCATION' in word and word[0].isupper():
    loc+=1
  elif '/ORGANIZATION' in word and word[0].isupper():
    org+=1
  elif '/PERSON' in word and word[0].isupper():
    per+=1
  elif word[0].isupper():
    tok+=1
  else:
    nor+=1
print
print
table = []
print "Total de palabras: " + str(loc+org+per+tok+nor)
print
table.append(["Location", loc])
table.append(["Organization", org])
table.append(["Person", per])
table.append(["Tokens", tok])
table.append(["Resto", nor])

print tabulate(table, headers=["Categoria", "Cantidad"], tablefmt="orgtbl")
print