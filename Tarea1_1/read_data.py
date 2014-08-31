import json
from tabulate import tabulate

CATEGORIES = {}
with open('categories.json', 'r') as file_:
  results = file_.read()
  CATEGORIES = json.loads(results)

with open('results.json', 'r') as file_:
  results = file_.read()
  data = json.loads(results)
  table = []
  for category in CATEGORIES:
    cat = CATEGORIES[category][0]
    if cat in data:
      per = data[cat]['Person']
      loc = data[cat]['Location']
      org = data[cat]['Organization']
      table.append([cat, per, loc, org])

  print "Cuenta:"
  print tabulate(table, headers=["Category","Person", "Location", 'Organization'], tablefmt="orgtbl")

print
with open('lemma.json', 'r') as file_:
  results = file_.read()
  data = json.loads(results)
  table = []
  for category in CATEGORIES:
    cat = CATEGORIES[category][0]
    if cat in data:
      per = data[cat]['Person']
      loc = data[cat]['Location']
      org = data[cat]['Organization']
      table.append([cat, per, loc, org])

  print "Cuenta lemmas:"
  print tabulate(table, headers=["Category","Person", "Location", 'Organization'], tablefmt="orgtbl")

