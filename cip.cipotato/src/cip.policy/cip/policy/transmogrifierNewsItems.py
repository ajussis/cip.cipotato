from collective.transmogrifier.interfaces import ISectionBlueprint, ISection
from zope.interface import classProvides, implements
from collective.transmogrifier.utils import defaultMatcher
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup
from collective.transmogrifier import utils
import sys
import re

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
            sys.setrecursionlimit(7000)
            item['_path'] = '/press-room/press-releases/' + item['id']
            item['_path'] = item['_path'].encode('ascii','ignore')
            print item
            yield item


class NewsItemSource(object):
    
    implements(ISection)
    classProvides(ISectionBlueprint)
    
    def __init__(self, transmogrifier, name, options, previous):
        self.options = options
        self.previous = previous
        pipeline = transmogrifier['transmogrifier']['pipeline']

        # options
        self.type = options.get('type', 'News Item')
        self.author = options.get('author', 'admin')

    def __iter__(self):
        for record in self.source():
            item = dict()
            item['_type'] = self.type
            item['creators'] = (self.author,)
            item['creation_date'] = record['pubdate']
            item['effectiveDate'] = record['pubdate']
            item['title'] = str(record['title'])
            item['description'] = str(record['description'])
            item['text'] = str(record['eng_content'])
            item['subject'] = (record['category'],)
            #import pdb; pdb.set_trace()
            #item['image'] = record['photo']
            item['_transitions'] = ('publish',)
            yield item

        for item in self.previous:
            yield item


    def source(self):
        xml = open("/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/pubimport/CGInsideNewsCIP2.xml")
        lines = xml.readlines()
        xml = '\n'.join(lines[1:])
        soupinit = BeautifulStoneSoup(xml)
        allNews = len(soupinit.findAll('item'))
        allFields = len(soupinit.contents[2])-1
        soup = BeautifulSoup(''.join(lines))
        newsList = {}
        for count in range(1, allNews, 2):
            if (soup.contents[0].contents[count].contents[34].string == 'True'):
                for field in range(1, allFields):
                    #import pdb; pdb.set_trace()
                    try:
                        newsList[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
                        newsname = soup.contents[0].contents[count].contents[field].name
                        newsstring = soup.contents[0].contents[count].contents[field].string
                        ns = newsstring
                        if ("[" in ns):
                            ns = ns.split("[")
                        if ("]" in ns):
                            ns = ns[2].split("]")
                            ns = ns[0]
                        if ("<strong>" in ns):
                            ns = ns.split("<strong>")
                            ns = ns[1]
                            ns = ns.split("</s")
                            ns = ns[0]
                        if ("<span style" in ns):
                            ns = ns.split(">")
                            ns = ns[1]
                            ns = ns.split("<s")
                            ns = ns[0]
                        ns = ns.replace('&ndash;','-')
                        ns = ns.replace('&nbsp;',' ')
                        ns = ns.replace('&nbsp',' ')
                        newsList[newsname] = ns
                    except:
                        continue
                yield newsList




"""

            try:
                newsList[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
                print newsList
            except:
                continue


            try:
                newsList[soup.contents[0].contents[count].contents[field].name]
                newsname = newsList[soup.contents[0].contents[count].contents[field].name]
                stringorig = soup.contents[0].contents[count].contents[field].string
                newsstring = re.stringorig('&nbsp','', s)
                print newsstring
                print newsname
                newsList[newsname] = newsstring
            except:
                continue


            try:
                newsList[soup.contents[0].contents[count].contents[field].name] = soup.contents[0].contents[count].contents[field].string
            except:
                continue

                yield newsList

digits3 = re.sub('9', '', digits2)
"""