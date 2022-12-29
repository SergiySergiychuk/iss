from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stopwords = stopwords.words()

def read_text_file(file_path):
  with open(file_path, 'r') as f:
    return f.read()

def format_document(text):
  #punctuation
  punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~\n'''
  for ele in text:  
    if ele in punc:  
      text = text.replace(ele, " ")
  text = text.lower()
  return text
          
def tokenize_document(text):
  for i in range(1):
    text_tokens = word_tokenize(text)
  return text_tokens

def remove_stopwords(tokens):
  purged_tokens = [word for word in tokens if not word in stopwords]
  return purged_tokens




def document_to_words(path):
  document       = read_text_file(path)
  formatted      = format_document(document)
  tokenized      = tokenize_document(formatted)
  cleaned_tokens = remove_stopwords(tokenized)
  return cleaned_tokens
