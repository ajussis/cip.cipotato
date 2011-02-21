from BeautifulSoup import BeautifulStoneSoup
xml = open("config.xml")
soup = BeautifulStoneSoup(xml)
for pub in soup.findAll('publication'):
#    import pdb; pdb.set_trace()
    for i in pub:
        print "tag: " + i.tag
        print "string:" + i.string

