from forward  import Forward
from inverted import Inverted
import docworks as dw

text1 = "You cannot just go in there blazing"
text2 = "We grab the choppers, go in guns blazing - simple as that"
text3 = "Do you really expect to just grab some choppers and go guns blazing?"

doc1 = dw.remove_stopwords(dw.tokenize_document(dw.format_document(text1)))
doc2 = dw.remove_stopwords(dw.tokenize_document(dw.format_document(text2)))
doc3 = dw.remove_stopwords(dw.tokenize_document(dw.format_document(text3)))

fwd = Forward()
ivt = Inverted()

fwd.append_entry("doc1", doc1)
fwd.append_entry("doc2", doc2)
fwd.append_entry("doc3", doc3)

ivt.append_entry("doc1", doc1)
ivt.append_entry("doc2", doc2)
ivt.append_entry("doc3", doc3)

ivt.print()

def test_fwd_append():
  assert any(fwd.dict["doc1"])
  assert fwd.dict["doc1"] == ['blazing']

  assert 'choppers' in fwd.dict["doc2"]
  assert 'guns', 'blazing' in fwd.dict["doc2"]
  assert 'guns', 'blazing' in fwd.dict["doc3"]
  
def test_ivt_append():
  assert any(ivt.dict["simple"])
  assert ivt.dict["simple"] == ["doc2"]

  assert "doc3" in ivt.dict["expect"]
  
  assert "doc1", "doc2" in ivt.dict["blazing"]
  assert "doc3" in ivt.dict["blazing"]
  
  assert "ludicrous" not in ivt.dict

def test_fwd_search():
  assert fwd.search('blazing')
  
  assert 'doc1', 'doc2' in fwd.search('blazing')
  assert 'doc3' in fwd.search('blazing')

  assert 'doc1', 'doc2' not in fwd.search('ludicrous')
  assert 'doc3' not in fwd.search('ludicrous')

  assert not fwd.search('ludicrous')

def test_ivt_search():
  assert ivt.search('blazing')
  
  assert 'doc1', 'doc2' in ivt.search('blazing')
  assert 'doc3' in ivt.search('blazing')

  assert 'doc1', 'doc2' not in ivt.search('ludicrous')  
  
test_fwd_append()
test_fwd_search()
test_ivt_append()
test_ivt_search()
