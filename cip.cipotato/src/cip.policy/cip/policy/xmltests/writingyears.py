import csv
dict2 = {'1924':'12/12/1924','2010':'4/5/2010','1994':'12/5/1994','1996':'12/5/1996'}

f = open('years.xml', 'w')
try:
    fieldnames = dict2.keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(dict2)
finally:
    f.close()

m = open('years.xml', 'rt').read()
dd = {}
ms = m.split(',')
ms[-1] = ms[-1][:-2]
for i in ms:
    dd[i[-4:]]=i.rsplit('/',1)[0]
dd['2001'] = '5/12'
f = open('years.xml', 'w')
ss = {}
try:
    fieldnames = dd.keys()
    for i in fieldnames:
        ss[i] = dd[i]+'/'+i
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(ss)
finally:
    f.close()
m = open('years.xml', 'rt').read()
dd = {}
ms = m.split(',')
ms[-1] = ms[-1][:-2]
print ms
for i in ms:
    dd[i[-4:]]=i.rsplit('/',1)[0]
print dd
