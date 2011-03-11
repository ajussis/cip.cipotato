"""Definition of the Publication content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from plone.app.blob.field import BlobField

# -*- Message Factory Imported Here -*-
from cip.ciptypes import ciptypesMessageFactory as _

from cip.ciptypes.interfaces import IPublication
from cip.ciptypes.config import PROJECTNAME

PublicationSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'author',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Author"),
            description=_(u"Author"),
        ),
    ),


    atapi.StringField(
        'pub_abstract',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Pub_Abstract"),
            description=_(u"Pub_Abstract"),
        ),
    ),


    atapi.StringField(
        'pub_salenote',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Pub_SaleNote"),
            description=_(u"Pub_SaleNote"),
        ),
    ),


    atapi.StringField(
        'pubstock',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"PubStock"),
            description=_(u"PubStock"),
        ),
    ),


    atapi.StringField(
        'pub_earthprint',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Pub_EarthPrint"),
            description=_(u"Pub_EarthPrint"),
        ),
    ),


    atapi.StringField(
        'pubcode',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"PubCode"),
            description=_(u"PubCode"),
        ),
    ),


    atapi.StringField(
        'pdf',
        storage=atapi.AnnotationStorage(),
        searchable=1,
        widget=atapi.StringWidget(
            label=_(u"PDF"),
            description=_(u"PDF"),
        ),
    ),


    atapi.StringField(
        'pubimage',
        storage=atapi.AnnotationStorage(),
        searchable=1,
        widget=atapi.StringWidget(
            label=_(u"Image"),
            description=_(u"Image"),
        ),
    ),


    atapi.StringField(
        'link',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Link"),
            description=_(u"Link"),
        ),
    ),


    atapi.StringField(
        'price',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Price"),
            description=_(u"Price"),
        ),
    ),


    atapi.StringField(
        'pages',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Pages"),
            description=_(u"Pages"),
        ),
    ),


    atapi.StringField(
        'issn',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"ISSN"),
            description=_(u"ISSN"),
        ),
    ),


    atapi.StringField(
        'isbn',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"ISBN"),
            description=_(u"ISBN"),
        ),
    ),


    atapi.StringField(
        'publisher',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Publisher"),
            description=_(u"Publisher"),
        ),
    ),


    atapi.StringField(
        'imprint',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Imprint"),
            description=_(u"Imprint"),
        ),
    ),


    atapi.StringField(
        'division',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Division"),
            description=_(u"Division"),
        ),
    ),


    atapi.StringField(
        'category',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Category"),
            description=_(u"Category"),
        ),
    ),


    atapi.StringField(
        'year',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Year"),
            description=_(u"Year"),
        ),
    ),


    atapi.StringField(
        'conference',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Conference"),
            description=_(u"Conference"),
        ),
    ),


    atapi.StringField(
        'series',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Series"),
            description=_(u"Series"),
        ),
    ),



))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PublicationSchema['title'].storage = atapi.AnnotationStorage()
PublicationSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(PublicationSchema, moveDiscussion=False)


class Publication(base.ATCTContent):
    """CIP Publication"""
    implements(IPublication)

    meta_type = "Publication"
    schema = PublicationSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    author = atapi.ATFieldProperty('author')

    pub_abstract = atapi.ATFieldProperty('pub_abstract')

    pub_salenote = atapi.ATFieldProperty('pub_salenote')

    pubstock = atapi.ATFieldProperty('pubstock')

    pub_earthprint = atapi.ATFieldProperty('pub_earthprint')

    pubcode = atapi.ATFieldProperty('pubcode')

    pdf = atapi.ATFieldProperty('pdf')

    pubimage = atapi.ATFieldProperty('pubimage')

    link = atapi.ATFieldProperty('link')

    price = atapi.ATFieldProperty('price')

    pages = atapi.ATFieldProperty('pages')

    issn = atapi.ATFieldProperty('issn')

    isbn = atapi.ATFieldProperty('isbn')

    publisher = atapi.ATFieldProperty('publisher')

    imprint = atapi.ATFieldProperty('imprint')

    division = atapi.ATFieldProperty('division')

    category = atapi.ATFieldProperty('category')

    year = atapi.ATFieldProperty('year')

    conference = atapi.ATFieldProperty('conference')

    series = atapi.ATFieldProperty('series')




atapi.registerType(Publication, PROJECTNAME)
