from BeautifulSoup import BeautifulStoneSoup
xml = open("config.xml")
soup = BeautifulStoneSoup(xml)
#import pdb; pdb.set_trace()
allPubs = len(soup.findAll('publication'))-1
allFields = len(soup.contents[0].contents[1])-1
d = {}
for count in range(1, allPubs,2):
    for field in range(1, allFields, 2):
        d[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
        print d

