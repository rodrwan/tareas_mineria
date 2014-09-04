import json
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
  DATA_PATH = './json_data/'
  VECT_PATH = './vectors/'
  onlyfiles = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
  CATEGORIES = {}
  with open('categories.json', 'r') as file_:
    results = file_.read()
    CATEGORIES = json.loads(results)

  bag_of_words = {}
  bag_of_keys = {}
  key_id = 0
  count_bow = 0
  cat_count = 1
  tokens = ['/ORGANIZATION', '/LOCATION', '/PERSON']
  ignore_files = ['.DS_Store', '.gitignore']
  for _file in onlyfiles:
    if _file not in ignore_files and '-key' not in _file:
      keys = {}
      sfile = _file.split('.')
      json_key_file = open(DATA_PATH+sfile[0]+'-key.'+sfile[1], 'r')
      keys = json.loads(json_key_file.read())
      json_feature_file = open(DATA_PATH+sfile[0]+'.'+sfile[1], 'r')
      features = json.loads(json_feature_file.read())
      end_file = open(VECT_PATH+sfile[0]+'-vec.txt', 'a')
      for feat_id in features:
        feature_1 = features[feat_id]['features_1']
        vector = str(feature_1['ES_TOKEN']) + ' '
        for feat_key in feature_1:
          if 'ES_TOKEN' not in feat_key and 'qid' not in feat_key:
            vector += str(keys[feat_key]) + ':' + str(feature_1[feat_key]) + ' '
          if 'PALABRA_' in feat_key:
            word = feat_key.split('PALABRA_')[1]
          if 'CAT_SINTACTICA_' in feat_key:
            cat = feat_key.split('CAT_SINTACTICA_')[1]
        vector += '# ' + feature_1['qid'] + ' ' + word + ' ' + cat
        print vector
        end_file.write(vector)
      end_file.close()
      break