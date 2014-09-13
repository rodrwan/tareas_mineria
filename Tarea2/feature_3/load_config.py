import json

class load_config:
  def __init__(self):
    self.conf_file = 'config.json'
    self.entities = []
    self.ignored_files = []
    self.categories = {}

  def read_config(self):
    with open(self.conf_file, 'r') as file_:
      results = file_.read()
      jtokens = json.loads(results)
      self.entities = jtokens['entities']
      self.ignored_files = jtokens['ignored_files']
      self.categories = jtokens['categories']

  def get_entities(self):
    return self.entities

  def get_ignored(self):
    return self.ignored_files

  def get_categories(self):
    return self.categories