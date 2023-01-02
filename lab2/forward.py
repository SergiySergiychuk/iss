import json

def append_entry(dict, document, keywords):
  if document not in dict:
    dict[document] = keywords
    
  elif document in dict:
    dict[document] += keywords
    dict[document] = list(set(dict[document]))
  
def print_dict(dict):
  print(json.dumps(dict, sort_keys=False, indent=2))
  
def search(index, query):
  pages = []
  for key in index.keys():
    if query in index[key]:
      pages.append(key)
  return pages
