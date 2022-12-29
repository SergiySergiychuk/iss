import json
  
class Inverted:
  dict = {}
  
  def append_entry_singular(self, keyword, document):
    if keyword not in self.dict:
      self.dict[keyword] = [document]
    
    elif keyword in self.dict:
      if document not in self.dict[keyword]:
        self.dict[keyword].append(document)
        
  def append_entry(self, document, keywords):
    for key in keywords:
      self.append_entry_singular(key, document)
  
  def print(self):
    print(json.dumps(self.dict, sort_keys=False, indent=2))
  
  def search(self, keyword):
    return self.dict[keyword]
