from BeautifulSoup import BeautifulSoup
file = open("publications.xml")
soup = BeautifulSoup(file)
pubnumber = len(soup("publication"))
print pubnumber
pubs = pubnumber / 10
return pubnumber % 10

"""pubid = "joo-nyt-testaillaan-kunnolla"
pubtitle = list(pubid)
m = 0
for i in pubtitle:
    if (i == "-"):
        pubtitle[m] = " "
    m = m+1
pubtitle = "".join(pubtitle).capitalize()
if (pubtitle == "Fact sheets flyer leaflet"):
    pubtitle = "Fact sheets & leaflets"
else:
    pubtitle = pubtitle + "s"
print pubtitle
"""

"""from BeautifulSoup import BeautifulStoneSoup
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

"""