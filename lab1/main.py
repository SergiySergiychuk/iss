import os
import docworks
from forward  import Forward
from inverted import Inverted

forward  = Forward()
inverted = Inverted()

path = os.getcwd() + "/documents"

documents = []

for file in os.listdir(path):
  if file.endswith(".txt"):
    file_path = f"{path}/{file}"
    tokens = docworks.document_to_words(file_path)
    doc_name = file[:-4]
    
    forward.append_entry(doc_name, tokens)
    inverted.append_entry(doc_name, tokens)


forward.print()
inverted.print()


print(forward.search("existence"))
print(inverted.search("existence"))

print(forward.search("neglected"))
print(inverted.search("neglected"))

##converting "documents" to strings to be fed into class methods 

# 0. Build unit-tests for the tasks below
# 1. Build forward index for a set of documents
# 2. Build inverted index  for a set of documents
# 3. Try to search information based on the indexes
