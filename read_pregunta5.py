import json
import operator
from tabulate import tabulate

sintactic_categories = {}
with open('sintactic_categories.json', 'r') as file_:
  content = file_.read()
  sintactic_categories = json.loads(content)

sorted_sc = sorted(sintactic_categories.iteritems(), key=operator.itemgetter(1), reverse=True)

table = []
for i in sorted_sc:
  table.append([i[0], i[1]])

print
print tabulate(table, headers=["Categoria","Cuenta"], tablefmt="orgtbl")
