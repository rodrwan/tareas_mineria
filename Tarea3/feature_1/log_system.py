import os
LOG_FILE = './logs/log.txt'
def read_log():
  # files = [ f for f in listdir(LOG_PATH) if isfile(join(LOG_PATH, f)) ]
  if os.path.exists(LOG_FILE):
    with open(LOG_FILE) as log_file:
      _file = log_file.read()
      return _file
  else:
    open(LOG_FILE, 'w').close()

def write_log(str):
  with open(LOG_FILE, 'w') as log_file:
    log_file.write(str)

def clear_log():
  open(LOG_FILE, 'w').close()