import json  
  
def append_entry_singular(dict, keyword, document):
  if keyword not in dict:
    dict[keyword] = [document]
  elif keyword in dict:
    if document not in dict[keyword]:
      dict[keyword].append(document)
      
def append_entry(dict, document, keywords):
  for key in keywords:
    append_entry_singular(dict, key, document)

def print_dict(dict):
  print(json.dumps(dict, sort_keys=False, indent=2))

def search(index, query):
  if query in index:
    return index[query]
  return []