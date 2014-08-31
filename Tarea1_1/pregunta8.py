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

left_org, left_loc, left_per, left_tok = {}, {}, {}, {}
right_org, right_loc, right_per, right_tok = {}, {}, {}, {}

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
          title = "#@#@ " + title.string + " @#@#"
          stitle = title.split()
          index = 0
          fin = len(stitle)-1

          for word in stitle:
            if index == fin:
              break
            lindex = index-1
            rindex = index+1

            if '/ORGANIZATION' in word:
              lword = stitle[lindex].split('/ORGANIZATION')[0].lower()
              if lword not in left_org:
                left_org[lword] = 1
              else:
                left_org[lword] += 1
              rword = stitle[rindex]
              if rword not in right_org:
                right_org[rword] = 1
              else:
                right_org[rword] += 1
            elif '/LOCATION' in word:
              lword = stitle[lindex].split('/LOCATION')[0].lower()
              if lword not in left_loc:
                left_loc[lword] = 1
              else:
                left_loc[lword] += 1
              rword = stitle[rindex]
              if rword not in right_loc:
                right_loc[rword] = 1
              else:
                right_loc[rword] += 1
            elif '/PERSON' in word:
              lword = stitle[lindex].split('/PERSON')[0].lower()
              if lword not in left_per:
                left_per[lword] = 1
              else:
                left_per[lword] += 1
              rword = stitle[rindex]
              if rword not in right_per:
                right_per[rword] = 1
              else:
                right_per[rword] += 1
            else:
              lword = stitle[lindex]
              if lword not in left_tok:
                left_tok[lword] = 1
              else:
                left_tok[lword] += 1
              rword = stitle[rindex]
              if rword not in right_tok:
                right_tok[rword] = 1
              else:
                right_tok[rword] += 1
            index += 1

        contents = y.findAll('content')
        for title in contents:
          title = "#@#@ " + title.string + " @#@#"
          stitle = title.split()
          index = 0
          fin = len(stitle)-1

          for word in stitle:
            if index == fin:
              break
            lindex = index-1
            rindex = index+1

            if '/ORGANIZATION' in word:
              lword = stitle[lindex].split('/ORGANIZATION')[0].lower()
              if lword not in left_org:
                left_org[lword] = 1
              else:
                left_org[lword] += 1
              rword = stitle[rindex]
              if rword not in right_org:
                right_org[rword] = 1
              else:
                right_org[rword] += 1
            elif '/LOCATION' in word:
              lword = stitle[lindex].split('/LOCATION')[0].lower()
              if lword not in left_loc:
                left_loc[lword] = 1
              else:
                left_loc[lword] += 1
              rword = stitle[rindex]
              if rword not in right_loc:
                right_loc[rword] = 1
              else:
                right_loc[rword] += 1
            elif '/PERSON' in word:
              lword = stitle[lindex].split('/PERSON')[0].lower()
              if lword not in left_per:
                left_per[lword] = 1
              else:
                left_per[lword] += 1
              rword = stitle[rindex]
              if rword not in right_per:
                right_per[rword] = 1
              else:
                right_per[rword] += 1
            else:
              lword = stitle[lindex]
              if lword not in left_tok:
                left_tok[lword] = 1
              else:
                left_tok[lword] += 1
              rword = stitle[rindex]
              if rword not in right_tok:
                right_tok[rword] = 1
              else:
                right_tok[rword] += 1
            index += 1

        answers = y.findAll('answer')
        for title in answers:
          title = "#@#@ " + title.string + " @#@#"
          stitle = title.split()
          index = 0
          fin = len(stitle)-1

          for word in stitle:
            if index == fin:
              break
            lindex = index-1
            rindex = index+1

            if '/ORGANIZATION' in word:
              lword = stitle[lindex].split('/ORGANIZATION')[0].lower()
              if lword not in left_org:
                left_org[lword] = 1
              else:
                left_org[lword] += 1
              rword = stitle[rindex]
              if rword not in right_org:
                right_org[rword] = 1
              else:
                right_org[rword] += 1
            elif '/LOCATION' in word:
              lword = stitle[lindex].split('/LOCATION')[0].lower()
              if lword not in left_loc:
                left_loc[lword] = 1
              else:
                left_loc[lword] += 1
              rword = stitle[rindex]
              if rword not in right_loc:
                right_loc[rword] = 1
              else:
                right_loc[rword] += 1
            elif '/PERSON' in word:
              lword = stitle[lindex].split('/PERSON')[0].lower()
              if lword not in left_per:
                left_per[lword] = 1
              else:
                left_per[lword] += 1
              rword = stitle[rindex]
              if rword not in right_per:
                right_per[rword] = 1
              else:
                right_per[rword] += 1
            else:
              lword = stitle[lindex]
              if lword not in left_tok:
                left_tok[lword] = 1
              else:
                left_tok[lword] += 1
              rword = stitle[rindex]
              if rword not in right_tok:
                right_tok[rword] = 1
              else:
                right_tok[rword] += 1
            index += 1

print
table = []
print "Vector contexto izquiero para 'organization'"
left_org = sorted(left_org.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]
for i in left_org:
  table.append([i[0], i[1]])
print tabulate(table, headers=["Palabra", "Cuenta"], tablefmt="orgtbl")
print
table = []
print "Vector contexto izquiero para 'location'"
left_loc =  sorted(left_loc.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]
for i in left_loc:
  table.append([i[0], i[1]])
print tabulate(table, headers=["Palabra", "Cuenta"], tablefmt="orgtbl")
print
table = []
print "Vector contexto izquiero para 'person'"
left_per = sorted(left_per.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]
for i in left_per:
  table.append([i[0], i[1]])
print tabulate(table, headers=["Palabra", "Cuenta"], tablefmt="orgtbl")
print
table = []
print "Vector contexto izquiero para 'tokens'"
left_tok = sorted(left_tok.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]
for i in left_tok:
  table.append([i[0], i[1]])
print tabulate(table, headers=["Palabra", "Cuenta"], tablefmt="orgtbl")
print
print "####################################################"
print
table = []
print "Vector contexto derecho para 'organization'"
left_org = sorted(right_org.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]
for i in left_org:
  table.append([i[0], i[1]])
print tabulate(table, headers=["Palabra", "Cuenta"], tablefmt="orgtbl")
print
table = []
print "Vector contexto derecho para 'location'"
left_loc =  sorted(right_loc.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]
for i in left_loc:
  table.append([i[0], i[1]])
print tabulate(table, headers=["Palabra", "Cuenta"], tablefmt="orgtbl")
print
table = []
print "Vector contexto derecho para 'person'"
left_per = sorted(right_per.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]
for i in left_per:
  table.append([i[0], i[1]])
print tabulate(table, headers=["Palabra", "Cuenta"], tablefmt="orgtbl")
print
table = []
print "Vector contexto derecho para 'tokens'"
left_tok = sorted(right_tok.iteritems(), key=operator.itemgetter(1), reverse=True)[0:5]
for i in left_tok:
  table.append([i[0], i[1]])
print tabulate(table, headers=["Palabra", "Cuenta"], tablefmt="orgtbl")