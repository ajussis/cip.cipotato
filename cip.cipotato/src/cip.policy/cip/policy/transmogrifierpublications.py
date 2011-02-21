from xml.etree import ElementTree as etree
from collective.transmogrifier.interfaces import ISectionBlueprint, ISection
from zope.interface import classProvides, implements
from collective.transmogrifier.utils import defaultMatcher

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
        
        # options
        self.container = options.get('container', 'person')
        
    def __iter__(self):

        for item in self.previous:
            item['_path'] = self.container + '/' + item['id']
            yield item


class PublicationSource(object):
    
    implements(ISection)
    classProvides(ISectionBlueprint)
    
    def __init__(self, transmogrifier, name, options, previous):
        self.options = options
        self.previous = previous
        
        # options
        self.type = options.get('type', 'Person')
        self.author = options.get('author', 'admin')

    def __iter__(self):


        for record in self.source():

            item = dict()
            
            # set general settings
            item['_type'] = self.type
            item['creators'] = (self.author,)           
            
            # set dates
            item['creation_date'] = record['date']
            item['effectiveDate'] = record['date']
            
            # set content fields
            item['title'] = record['title']
            item['text'] = record['text']
            item['subject'] = (record['category'],)
            
            # publish news item
            item['_transitions'] = ('publish',)
            
            yield item
            
        for item in self.previous:
            yield item


    def source(self):
        """A method that parses raw data and returns results.
        You can parse data from HTML document, CSV, JSON, etc. 
        Your options are virtually limitless.
        
        Check out real-world examples can be found in /branches of this product's repository.
        """

#        import pdb; pdb.set_trace()
        
        categories = ["anual_report.xml", "brochures_fact_sheets.xml"]

        route = '/home/ajussis/Develop/cip.cipotato/cip.cipotato/src/cip.policy/cip/policy/'+categories[0]
        file = route

        list = {'list': [
                    {'publication':
                        [{'author': 'Centro Internacional de la Papa (CIP)'},
                         {'title': 'Papa madre. Historia de una exposicion fotografica. History of a photographic exhibition'},
                         {'series': {}},
                         {'conference': {}},
                         {'year': '2009'},
                         {'category': 'Book'},
                         {'division': {}},
                         {'imprint': {}},
                         {'publisher': 'Centro Internacional de la Papa'},
                         {'isbn': '978-92-9060-376-4'},
                         {'issn': {}},
                         {'pages': '151'},
                         {'price': '30.00'},
                         {'link': {}},
                         {'image': '004755.jpg'},
                         {'pdf': {}},
                         {'PubCode': '004755'},
                         {'Pub_EarthPrint': {}},
                         {'PubStock': '999'},
                         {'Pub_SaleNote': {}},
                         {'Pub_Abstract': {}}
                        ]
                    },
                    {'publication': [{'author': 'Graves, C. (ed.).'}, {'title': 'La papa tesoro de los Andes. De la agricultura  a la cultura.  (Reimpresion Nov 2006)'}, {'series': {}}, {'conference': {}}, {'year': '2006'}, {'category': 'Book'}, {'division': {}}, {'imprint': {}}, {'publisher': 'Centro Internacional de la Papa'}, {'isbn': '92-9060-204-X'}, {'issn': {}}, {'pages': '210'}, {'price': '60.00'}, {'link': 'http://www.cipotato.org/publications/books/papa_tesoro_andes_online/'}, {'image': '003793.jpg'}, {'pdf': {}}, {'PubCode': '003793'}, {'Pub_EarthPrint': 'http://www.earthprint.com/productfocus.php?id=CIP027'}, {'PubStock': '827'}, {'Pub_SaleNote': {}}, {'Pub_Abstract': {}}]}, {'publication': [{'author': 'Balbotin Arenas, P.'}, {'title': 'I custodi della biodiversita / The custodians of biodiversity / Los custodios de la biodiversidad.'}, {'series': {}}, {'conference': {}}, {'year': '2003'}, {'category': 'Book'}, {'division': {}}, {'imprint': {}}, {'publisher': 'Edizioni Angolo Manzoni; FAO; Istituto Agronomico per l&#39;Otremare; CIP; Fondazione Italiana La Fotografia; Forum di Associazioni per la cultura.'}, {'isbn': '88-861142-95-1'}, {'issn': {}}, {'pages': '168'}, {'price': '30.00'}, {'link': {}}, {'image': '002711.jpg'}, {'pdf': {}}, {'PubCode': '002711'}, {'Pub_EarthPrint': 'http://www.earthprint.com/product.aspx?id=4217'}, {'PubStock': '374'}, {'Pub_SaleNote': {}}, {'Pub_Abstract': {}}]}, {'publication': [{'author': 'Centro Internacional de la Papa (CIP); FEDECCH, Federacion Departamental de Comunidades Campesinas de Huancavelica'}, {'title': 'Catalogo de variedades de papa nativa de Huancavelica-Peru'}, {'series': {}}, {'conference': {}}, {'year': '2006'}, {'category': 'Catalog'}, {'division': {}}, {'imprint': {}}, {'publisher': 'Centro Internacional de la Papa'}, {'isbn': '92-9060-274-0'}, {'issn': {}}, {'pages': '206'}, {'price': '30.00'}, {'link': {}}, {'image': '003524.jpg'}, {'pdf': '003524.pdf'}, {'PubCode': '003524'}, {'Pub_EarthPrint': 'http://www.earthprint.com/product.aspx?id=4228'}, {'PubStock': '377'}, {'Pub_SaleNote': {}}, {'Pub_Abstract': {}}]}]}


"""from xml.etree import ElementTree as etree

file = open("best_sellers.xml")
tree = etree.parse(file)
el = tree.getroot()

def xml_to_dict(el):
    d={}
    if el.text:
        d[el.tag] = el.text
    else:
        d[el.tag] = {}
    children = el.getchildren()
    if children:
        d[el.tag] = map(xml_to_dict, children)
    return d

xml_to_dict(el)
"""
"""
def source():
    for count in range(1, 6):
        result = dict(title = 'news item %i' %count, category = 'category %i' %count,date = '2010/01/0%i' %count,text = 'bolded number: <b>%i</b>' %count,)
        yield result"""
            