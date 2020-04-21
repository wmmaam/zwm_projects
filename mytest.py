import pandas as pd

l = ["jim", "sarah", "cook"]
dct = {'a': 'jim', 'b': 'sarah', 'c': 'jim'}
s = pd.Series(dct)

s = s.append(pd.Series("anderson"), ignore_index=False)
# print(s['a'])
# print(s.T)

d = pd.DataFrame(s)
d.columns = ['thenames']
col = d['thenames']

# print(type(col))
# help(pd.DataFrame.__getitem__)

cts = col.value_counts()
# print('HELP.......')
# help(col.value_counts)
# print('HELP.......end')
# print(cts)
# print(d.T)

# somevar = "ddfddfd"
# somevar = 21321

print(cts)