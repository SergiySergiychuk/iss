import os
import sys

import docworks
import inverted

name = False
mode = False
path = ''
filenames = []
index = {}
file_titles = {}
query = ''
query_res = []

if len(sys.argv) > 1 and sys.argv[1]:
  name = sys.argv[1]

if len(sys.argv) > 2 and sys.argv[2]:
  if sys.argv[2] == "-s":
    mode = True

if name:
  path = "./" + name
  for file in os.listdir(path):
    if file.endswith(".txt"):
      file_path = f"{path}/{file}"
      filenames.append(file_path)

  docworks.create_index(filenames, index, file_titles)
  inverted.print_dict(index)
  print(file_titles)

if mode:
  query = input("Query (empty to stop): ")
  if query != "\n":
    query_res = inverted.search(index, query)
    if len(query_res) > 0:
      for doc in query_res:
        print(f'Title: "{file_titles[doc]}", File: {doc}')
    else:
      print("None found")
