import json
from os import listdir
from os.path import isfile, join
import MontyLemmatiser
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
lemma = sys.argv[1]
if lemma == "lemma":
  result_lemma = {}
  p = MontyLemmatiser.MontyLemmatiser()

table = []
tablelema = []
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
      if lemma == "lemma":
        result_lemma[category] = {
          "Person": 0,
          "Location": 0,
          "Organization": 0
        }
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
          title = title.string
          loc += int(str(title).count('/LOCATION'))
          org += int(str(title).count('/ORGANIZATION'))
          per += int(str(title).count('/PERSON'))
          if lemma == "lemma":
            aux_string = title.split()
            words_with_label_loc = [x.replace("/LOCATION", "") for x in aux_string if '/LOCATION' in x]
            words_with_label_org = [x.replace("/ORGANIZATION", "") for x in aux_string if '/ORGANIZATION' in x]
            words_with_label_per = [x.replace("/PERSON", "") for x in aux_string if '/PERSON' in x]
            Str = title.replace("/LOCATION", "").replace("/ORGANIZATION", "").replace("/PERSON", "")
            newString = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), Str.split())
            for ns in newString:
              for wll in words_with_label_loc:
                if ns == wll:
                  lem_loc += 1
              for wlo in words_with_label_org:
                if ns == wlo:
                  lem_org += 1
              for wlp in words_with_label_per:
                if ns == wlp:
                  lem_per += 1
          # print " ".join(newString).encode('utf-8')
        contents = y.findAll('content')
        for content in contents:
          content = content.string
          loc += int(str(content).count('/LOCATION'))
          org += int(str(content).count('/ORGANIZATION'))
          per += int(str(content).count('/PERSON'))
          if lemma == "lemma":
            aux_string = content.split()
            words_with_label_loc = [x.replace("/LOCATION", "") for x in aux_string if '/LOCATION' in x]
            words_with_label_org = [x.replace("/ORGANIZATION", "") for x in aux_string if '/ORGANIZATION' in x]
            words_with_label_per = [x.replace("/PERSON", "") for x in aux_string if '/PERSON' in x]
            Str = content.replace("/LOCATION", "").replace("/ORGANIZATION", "").replace("/PERSON", "")
            newString = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), Str.split())
            for ns in newString:
              for wll in words_with_label_loc:
                if ns == wll:
                  lem_loc += 1
              for wlo in words_with_label_org:
                if ns == wlo:
                  lem_org += 1
              for wlp in words_with_label_per:
                if ns == wlp:
                  lem_per += 1
        answers = y.findAll('answer')
        for answer in answers:
          answer = answer.string
          loc += int(str(answer).count('/LOCATION'))
          org += int(str(answer).count('/ORGANIZATION'))
          per += int(str(answer).count('/PERSON'))
          if lemma == "lemma":
            aux_string = answer.split()
            words_with_label_loc = [x.replace("/LOCATION", "") for x in aux_string if '/LOCATION' in x]
            words_with_label_org = [x.replace("/ORGANIZATION", "") for x in aux_string if '/ORGANIZATION' in x]
            words_with_label_per = [x.replace("/PERSON", "") for x in aux_string if '/PERSON' in x]
            Str = answer.replace("/LOCATION", "").replace("/ORGANIZATION", "").replace("/PERSON", "")
            newString = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), Str.split())
            for ns in newString:
              for wll in words_with_label_loc:
                if ns == wll:
                  lem_loc += 1
              for wlo in words_with_label_org:
                if ns == wlo:
                  lem_org += 1
              for wlp in words_with_label_per:
                if ns == wlp:
                  lem_per += 1

      results[category]["Person"] = per
      results[category]["Location"] = loc
      results[category]["Organization"] = org
      if lemma == "lemma":
        result_lemma[category]["Person"] = lem_per
        result_lemma[category]["Location"] = lem_loc
        result_lemma[category]["Organization"] = lem_org

      table.append([category, per, loc, org])
      tablelema.append([category, lem_per, lem_loc, lem_org])
      # print "Person: " + str(per) + "/" + str(lem_per)
      # print "Location: " + str(loc) + "/" + str(lem_loc)
      # print "Organization: " + str(org) + "/" + str(lem_org)
print


import json
# print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))
with open('results.json', 'w') as file_:
    file_.write(json.dumps(results, sort_keys=True, indent=4, separators=(',', ': ')))
if lemma == "lemma":
#   print json.dumps(result_lemma, sort_keys=True, indent=4, separators=(',', ': '))
  with open('lemma.json', 'w') as file_:
      file_.write(json.dumps(result_lemma, sort_keys=True, indent=4, separators=(',', ': ')))

print "Cuenta"
print tabulate(table, headers=["Category","Person", "Location", 'Organization'], tablefmt="pipe")
print
print "Cuenta con lemmas:"
print tabulate(tablelema, headers=["Category","Person", "Location", 'Organization'], tablefmt="pipe")



