from tika import parser

raw = parser.from_file('text1.pdf')
s = (raw['content'])
s = str(s)
s = s.replace(",","")
s = s.replace(".","")
print (s)
