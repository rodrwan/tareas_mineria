from utils import is_capitalized, full_upper, full_lower, has_root, sin_cat, word_len
import json
import sys

def all_occurences(stext, word):
  index = 0
  idx_list = []
  for st in stext:
    if st == word:
      idx_list.append(index)
    index += 1
  return idx_list

def create_side(words, side, tmp_bow, text, entities, tag, token):
  if side == 'left':
    key = 'IZQUIERDA_'
    key_cat = 'IZQUIERDA_CAT_'
  elif side == 'right':
    key = 'DERECHA_'
    key_cat = 'DERECHA_CAT_'

  for w in words:
    try:
      key_word = key.encode('utf-8')+str(w.encode('utf-8'))
    except:
      pass
    # cat = sin_cat(w, text, entities)
    try:
      tag = tag[tag.index(w):len(tag)]
    except:
      tag = w+'/.'
    try:
      tag = tag[0:tag.index(' ')]
    except:
      tag = tag[0:]
    stag =tag.split('/')
    try:
      cat = stag[1]
    except:
      cat = '.'
    if cat in [',', '.']:
      cat = 'PUNCT'
    key_cat_tmp = key_cat+cat

    if key_cat_tmp in tmp_bow:
      tmp_bow[key_cat_tmp] += 1
    else:
      tmp_bow[key_cat_tmp] = 1
    if key_word in tmp_bow:
      tmp_bow[key_word] += 1
    else:
      tmp_bow[key_word] = 1
  tmp_bow['ES_TOKEN'] = token
  return tmp_bow

def create_main_feature(qid, word, token, text, entities, tags):
  tmp_bow = {}
  tmp_bow['qid'] = qid
  tmp_bow['TIENE_RAIZ'] = has_root(word)
  tmp_bow['FULL_MAYUSCULAS'] = full_upper(word)
  tmp_bow['FULL_MINUSCULAS'] = full_lower(word)
  tmp_bow['INICIO_MAYUSCULAS_RESTO_MINUSCULAS'] = is_capitalized(word)
  # print word.encode('utf-8')
  cat = sin_cat(word, tags)
  tmp_bow['CAT_SINTACTICA_' + cat] = 1
  tmp_bow['PALABRA_'+word] = 1
  tmp_bow['PALABRA_LARGO'] = word_len(word)
  tmp_bow['ES_TOKEN'] = token
  return tmp_bow

def create_second_feature(qid, word, text, entities, index, tags, token):
  # this function processes the context of the word,
  #  we analyze the right and left side of the word,
  #  try to look the features of the word that we find.
  tmp_bow = {}
  stext = text.split()
  # left side
  words = []
  words.append(stext[index-3])
  words.append(stext[index-2])
  words.append(stext[index-1])
  tmp_bow['qid'] = qid
  tmp_bow = create_side(words, 'left', tmp_bow, text, entities, tags, token)
  # right side
  words = []
  words.append(stext[index+3])
  words.append(stext[index+2])
  words.append(stext[index+1])
  tmp_bow = create_side(words, 'right', tmp_bow, text, entities, tags, token)
  return tmp_bow

def create_third_feature(word, text):
  #  this function processes the context of the word,
  #  we analyze the right and left side of the word,
  #  try to look the features of the word that we find.
  #  Same as previous function but new we look on the global scope.
  tmp_bow = {}
  stext = text.split()
  index = all_occurences(stext, word)
  for idx in index:
    # left side
    words = []
    words.append(stext[idx-3])
    words.append(stext[idx-2])
    words.append(stext[idx-1])
    tmp_bow = create_side(words, 'left', tmp_bow)
    # right side
    words = []
    words.append(stext[index+3])
    words.append(stext[index+2])
    words.append(stext[index+1])
    tmp_bow = create_side(words, 'right', tmp_bow)
  return tmp_bow

def create_fourth_feature():
  pass



