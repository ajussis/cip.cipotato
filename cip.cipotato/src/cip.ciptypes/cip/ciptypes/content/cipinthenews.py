"""Definition of the CIP in the News content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.ciptypes import ciptypesMessageFactory as _

from cip.ciptypes.interfaces import ICIPintheNews
from cip.ciptypes.config import PROJECTNAME

CIPintheNewsSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'newsurl',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"URL"),
            description=_(u"URL address for the news item"),
        ),
        required=True,
        validators=('isURL'),
    ),


    atapi.DateTimeField(
        'pubdate',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Publication date"),
            description=_(u"The date when the news was originally published"),
        ),
        required=True,
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'mediasource',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Media source"),
            description=_(u"Add the name of the media organization"),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CIPintheNewsSchema['title'].storage = atapi.AnnotationStorage()
CIPintheNewsSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CIPintheNewsSchema, moveDiscussion=False)


class CIPintheNews(base.ATCTContent):
    """A content type to add external media articles"""
    implements(ICIPintheNews)

    meta_type = "CIPintheNews"
    schema = CIPintheNewsSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    newsurl = atapi.ATFieldProperty('newsurl')

    pubdate = atapi.ATFieldProperty('pubdate')

    mediasource = atapi.ATFieldProperty('mediasource')


atapi.registerType(CIPintheNews, PROJECTNAME)
