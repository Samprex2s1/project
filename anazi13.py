import rutermextract
from rutermextract import TermExtractor
term_extractor = TermExtractor()
strings = True
spisok = []
text = u'text'
for term in term_extractor(text):
    spisok.append(term.normalized)
print(spisok, type(spisok[1]))
