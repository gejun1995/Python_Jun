import re

a = ">Cluster-101346.150239_1"
pattern = re.compile(r'Cluster-\d*.\d*')
a1 = pattern.findall(a)
print(a1)

b = ['1', '2', '3']
c = ['3', '4', '5']
d = set(b) | set(c)
e = set(b) & set(c)
f = (set(b) | set(c)) - (set(b) & set(c))

print(d)
print(e)
print(f)

