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

results = {}
import sys
table = []

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
      loc, org, per = 0.0, 0.0, 0.0
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
        if nel[0].isupper():
          loc+=1.

      for neo in name_entites_org:
        if neo[0].isupper():
          org+=1.

      for nep in name_entites_per:
        if nep[0].isupper():
          per+=1.


      try:
        locc = "{0:.2f}%".format(100*loc/len(name_entites_loc))
        orgc = "{0:.2f}%".format(100*org/len(name_entites_org))
        perc = "{0:.2f}%".format(100*per/len(name_entites_per))
      except:
        locc, orgc, perc = 0, 0, 0
      table.append([category, perc, locc, orgc])
print


print "Mayusculas por clase:"
print tabulate(table, headers=["Category","Person", "Location", 'Organization'], tablefmt="orgtbl")


