from collective.transmogrifier.interfaces import ISectionBlueprint, ISection
from zope.interface import classProvides, implements
from collective.transmogrifier.utils import defaultMatcher
from BeautifulSoup import BeautifulStoneSoup
from collective.transmogrifier import utils
import sys

class FormatSetter(object):

    implements(ISection)
    classProvides(ISectionBlueprint)

    def __init__(self, transmogrifier, name, options, previous):
        self.options = options
        self.previous = previous
        self.context = transmogrifier.context
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')

        # options
        self.format = options.get('format', 'text/html')

    def __iter__(self):

        for item in self.previous:
            pathkey = self.pathkey(*item.keys())[0]
            if not pathkey: # not enough info
                yield item; continue
            path = item[pathkey]
        
            ob = self.context.unrestrictedTraverse(path.lstrip('/'), None)
            if ob is None:
                yield item; continue # object not found

            ob.setFormat(self.format)
            ob.setContentType(self.format)

            yield item


class PathSetter(object):

    implements(ISection)
    classProvides(ISectionBlueprint)

    def __init__(self, transmogrifier, name, options, previous):
        self.options = options
        self.previous = previous
        
    def __iter__(self):

        for item in self.previous:
            categ = item['category'].lower()
            categ = categ.replace(' ','-')
            categ = categ.replace('/-','')
            sys.setrecursionlimit(7000)
            #import pdb; pdb.set_trace()
            item['_path'] = '/resources/publications/' + categ + '/' + item['id']
            item['_path'] = item['_path'].encode('ascii','ignore')
            print item
            yield item


class PublicationSource(object):
    
    implements(ISection)
    classProvides(ISectionBlueprint)
    
    def __init__(self, transmogrifier, name, options, previous):
        self.options = options
        self.previous = previous
        pipeline = transmogrifier['transmogrifier']['pipeline']

        # options
        self.type = options.get('type', 'Publication')
        self.author = options.get('author', 'admin')

    def __iter__(self):
        """
        divpubs = self.getallpubnumber()
        divpubs = divpubs / 15
        count = 1
        lastcount = divpubs % 15
        for i in range(1,15):
        """
        for record in self.source():
            item = dict()
            item['_type'] = self.type
            item['creators'] = (self.author,)
            item['title'] = str(record['title']).strip("<![CDATA[")[:-3]
            item['author'] = str(record['author']).strip("<![CDATA[")[:-3]
            item['series'] = str(record['series']).strip("<![CDATA[")[:-3]
            item['category'] = record['category']
            item['conference'] = str(record['conference']).strip("<![CDATA[")[:-3]
            if record.get('division',None) is not None:
                item['division'] = record['division']
            item['year'] = record['year']
            item['creation_date'] = record['creation_date']
            item['effectiveDate'] = record['creation_date']
            item['imprint'] = str(record['imprint']).strip("<![CDATA[")[:-3]
            item['publisher'] = str(record['publisher']).strip("<![CDATA[")[:-3]
            item['isbn'] = record['isbn']
            item['issn'] = record['issn']
            item['pages'] = record['pages']
            item['price'] = record['price']
            item['link'] = str(record['link']).strip("<![CDATA[")[:-3]
            item['pubimage'] = record['image']
            item['pdf'] = record['pdf']
            item['pubcode'] = record['pubcode']
            item['pub_earthprint'] = str(record['pub_earthprint']).strip("<![CDATA[")[:-3]
            item['pubstock'] = record['pubstock']
            item['pub_salenote'] = str(record['pub_salenote']).strip("<![CDATA[")[:-3]
            item['pub_abstract'] = str(record['pub_abstract']).strip("<![CDATA[")[:-3]
            item['_transitions'] = ('publish',)
            yield item

        for item in self.previous:
            yield item

    """
    def getallpubnumber(self):
        xml = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/pubimport/publications.xml")
        soup = BeautifulStoneSoup(xml)
        return len(soup("publication"))


    def source(self,pubcount, pubend):
        xml = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/pubimport/publications.xml")
        lines = xml.readlines()
        xml = '\n'.join(lines[1:])
        soup = BeautifulStoneSoup(xml)
        #allPubs = len(soup.findAll('publication'))

        allFields = len(soup.contents[0].contents[1])-1
        d = {}
        list = []
        """
    """
        1,50  1-51     (pubend*(pubcount-1)+1, pubend*pubcount+1)
        2,50  51-101   (pubend*(pubcount-1)+1, pubend*pubcount+1)
        3,50  101-151  (pubend*(pubcount-1)+1,
        4,50  201-251  (pubend*(pubcount-1)+1,

        1,51  1-51     (pubend*(pubcount-1)+1, pubend*pubcount+1)
        2,51  51-101   (pubend*(pubcount-1)+1, pubend*pubcount+1)
        3,51  101-151  (pubend*(pubcount-1)+1,
        4,51  201-251  (pubend*(pubcount-1)+1,

    """
    """
        #import pdb; pdb.set_trace()
        if (pubend % 2 != 0):
            pubend = pubend - 1
        for count in range(pubend*(pubcount-1)+1, pubend*pubcount+1, 2):
            for field in range(1, allFields, 2):
                d[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
            yield d
    """

    def source(self):
        xml = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/pubimport/publications.xml")
        lines = xml.readlines()
        xml = '\n'.join(lines[1:])
        soup = BeautifulStoneSoup(xml)
        allPubs = len(soup.findAll('publication'))
        allFields = len(soup.contents[0].contents[1])-1
        d = {}
        list = []
        d = 1
        m = 1
        year
        #import pdb; pdb.set_trace()
        for count in range(1, allPubs,2):
            for field in range(1, allFields, 2):
                if (soup.contents[0].contents[count].contents[field].name == 'year'):

                    d["creation_date"] = d+'/'+m+'/'+year
                    d = d+1
                    m = m+1
                    if d = 28
                d[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
            yield d
