from BeautifulSoup import BeautifulStoneSoup
import sys
import csv
xml = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/pubimport/publications.xml")
lines = xml.readlines()
xml.close()
xml = '\n'.join(lines[1:])
soup = BeautifulStoneSoup(xml)
allPubs = len(soup.findAll('publication'))
allFields = len(soup.contents[0].contents[1])-1
print "allPubs: ", allPubs
print "allFields: ", allFields
pubdict = {}
list = []
testlist = []
d = 1
m = 1
pubcount = 1
year = 1978
for count in range(1, allPubs*2,2):
    print "pubcount: ", pubcount
    pubcount += 1
    for field in range(1, allFields, 2):
        if (soup.contents[0].contents[count].contents[field].name == 'year'):
            years = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/pubimport/years.csv", "rt").read()
            yearstowrite = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/pubimport/years.csv", "w")
            dd = {}
            ms = years.split(',')
            ms[-1] = ms[-1][:-2]
            for i in ms:
                dd[i[-4:]]=i.rsplit('/',1)[0]
            yearstring = soup.contents[0].contents[count].contents[field].string
            try:
                yd = dd[yearstring]
                d = int(yd.split('/')[0])+1
                m = int(yd.split('/')[1])
            except:
                dd[yearstring] = '1/1'
            if (m != 2 and d > 27):
                d = 1
                m = m + 1
            if (m > 11 and d > 26):
                m = 1
            pubdict["creation_date"] = str(d)+'/'+str(m)+'/'+soup.contents[0].contents[count].contents[field].string
            dd[yearstring] = str(d)+'/'+str(m)
            ss = {}
            try:
                fieldnames = dd.keys()
                for i in fieldnames:
                    if (i != ''):
                        ss[i] = dd[i]+'/'+i
                writer = csv.DictWriter(yearstowrite, fieldnames=fieldnames)
                writer.writerow(ss)
                print ss
            finally:
                yearstowrite.close()
        pubdict[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
    testlist.append(pubdict)
    print "testlist: ", testlist