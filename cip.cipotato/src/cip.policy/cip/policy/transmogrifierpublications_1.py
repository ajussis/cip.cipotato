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
        xml = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/config.xml")
        soup = BeautifulStoneSoup(xml)
        allPubs = len(soup.findAll('publication'))-1
        allFields = len(soup.contents[0].contents[1])-1
        d = {}
        list = []
        for count in range(1, allPubs,2):
            for field in range(1, allFields, 2):
                d[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
                list.append(d)

        for record in list:"""

        for record in self.source():

            item = dict()

            item['_type'] = self.type
            item['creators'] = (self.author,)

            # set dates
            #item['creation_date'] = record['year']
            #item['effectiveDate'] = record['year']

            # set content fields
            item['title'] = record['title']
            #item['subject'] = (record['category'],)
            item['author'] = record['author']
            item['series'] = record['series']
            #import pdb; pdb.set_trace()
            item['category'] = record['category']
            item['conference'] = record['conference']
            #import pdb; pdb.set_trace()
            if record.get('division',None) is not None:
                item['division'] = record['division']
            item['year'] = record['year']
            item['imprint'] = record['imprint']
            item['publisher'] = record['publisher']
            item['isbn'] = record['isbn']
            item['issn'] = record['issn']
            item['pages'] = record['pages']
            item['price'] = record['price']
            item['link'] = record['link']
            #item['_image'] = self.image
            item['pdf'] = record['pdf']
            item['pubcode'] = record['pubcode']
            item['pub_earthprint'] = record['pub_earthprint']
            item['pubstock'] = record['pubstock']
            item['pub_salenote'] = record['pub_salenote']
            item['pub_abstract'] = record['pub_abstract']
            
            # publish news item
            item['_transitions'] = ('publish',)

            yield item

        for item in self.previous:
            yield item

    def source(self):
        xml = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/pubimport/publications_1.xml")
        lines = xml.readlines()
        xml = '\n'.join(lines[1:])
        soup = BeautifulStoneSoup(xml)
        allPubs = len(soup.findAll('publication'))
        allFields = len(soup.contents[0].contents[1])-1
        d = {}
        list = []
        #import pdb; pdb.set_trace()
        for count in range(1, allPubs,2):
            for field in range(1, allFields, 2):
                d[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
            yield d
