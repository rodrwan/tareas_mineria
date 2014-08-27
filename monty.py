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

results = {}
import sys
table = []
table_cls = []
p = MontyLemmatiser.MontyLemmatiser()
loc, org, per = 0.0, 0.0, 0.0
for _file in onlyfiles:
  if _file != '.DS_Store':
    if (CATEGORIES[_file][1] == "Done"):
      category = CATEGORIES[_file][0]
      # print "##################################"
      # print "Category: " + category
      file_name = DATA_PATH + _file
      results[category] = {
        "Person": 0,
        "Location": 0,
        "Organization": 0
      }

      f = open(file_name, 'r')
      content = f.read()
      y = BeautifulSoup(content)
      questions = y.findAll('question')
      name_entites_loc = []
      name_entites_org = []
      name_entites_per = []

      for question in questions:
        y = BeautifulSoup(str(question))
        titles = y.findAll('title')
        for title in titles:
          title = title.string
          aux_string = title.split()
          name_entites_loc += [x.replace("/LOCATION", "") for x in aux_string if '/LOCATION' in x]
          name_entites_org += [x.replace("/ORGANIZATION", "") for x in aux_string if '/ORGANIZATION' in x]
          name_entites_per += [x.replace("/PERSON", "") for x in aux_string if '/PERSON' in x]

        contents = y.findAll('content')
        for content in contents:
          content = content.string
          aux_string = content.split()
          name_entites_loc += [x.replace("/LOCATION", "") for x in aux_string if '/LOCATION' in x]
          name_entites_org += [x.replace("/ORGANIZATION", "") for x in aux_string if '/ORGANIZATION' in x]
          name_entites_per += [x.replace("/PERSON", "") for x in aux_string if '/PERSON' in x]
        answers = y.findAll('answer')

        for answer in answers:
          answer = answer.string
          aux_string = answer.split()
          name_entites_loc += [x.replace("/LOCATION", "") for x in aux_string if '/LOCATION' in x]
          name_entites_org += [x.replace("/ORGANIZATION", "") for x in aux_string if '/ORGANIZATION' in x]
          name_entites_per += [x.replace("/PERSON", "") for x in aux_string if '/PERSON' in x]

      for nel in name_entites_loc:
        newString = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), [nel])
        if nel != newString[0]:
          loc+=1
          table.append([nel, newString[0].encode('utf-8')])

      for neo in name_entites_org:
        newString = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), [neo])
        if neo != newString[0]:
          org+=1
          table.append([neo, newString[0].encode('utf-8')])

      for nep in name_entites_per:
        newString = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), [nep])
        if nep != newString[0]:
          per += 1
          table.append([nep, newString[0].encode('utf-8')])
table_cls.append([per, loc, org])

print
print tabulate(table, headers=["Entidad","Lema"], tablefmt="pipe")
print

print "Clases con mayores cambios:"
print tabulate(table_cls, headers=["Person", "Location", 'Organization'], tablefmt="pipe")
