import re

pattern = re.compile(r'([a-zA-Z=]).([a])')

string = 'search this inside of this text please'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(d)
print(b)
print(c)
print(a.span())

print(a.start())

print(a.group(2))