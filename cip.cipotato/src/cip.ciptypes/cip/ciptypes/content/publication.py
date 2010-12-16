"""Definition of the Publication content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from plone.app.blob.field import BlobField, ImageField

# -*- Message Factory Imported Here -*-
from cip.ciptypes import ciptypesMessageFactory as _

from cip.ciptypes.interfaces import IPublication
from cip.ciptypes.config import PROJECTNAME

PublicationSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'type',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Publication type"),
            description=_(u"Add the type of the publication (book, working paper)"),
        ),
    ),

    ImageField(
        'coverimage',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Cover Image"),
            description=_(u"Insert the publication's cover image"),
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
    type = atapi.ATFieldProperty('type')

    coverimage = atapi.ATFieldProperty('coverimage')


atapi.registerType(Publication, PROJECTNAME)
