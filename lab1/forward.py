import json

class Forward:
  dict = {}
  
  def append_entry(self, document, keywords):
    if document not in self.dict:
      self.dict[document] = keywords
      
    elif document in self.dict:
      #add new and remove duplicates
      self.dict[document] += keywords
      self.dict[document] = list(set(self.dict[document]))
    
  def print(self):
    print(json.dumps(self.dict, sort_keys=False, indent=2))
    
  def search(self, keyword):
    pages = []
    for key in self.dict.keys():
      if keyword in self.dict[key]:
        pages.append(key)
    return pages
