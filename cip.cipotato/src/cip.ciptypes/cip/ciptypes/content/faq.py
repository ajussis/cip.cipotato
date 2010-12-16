"""Definition of the FAQ content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import IFAQ
from cip.ciptypes.config import PROJECTNAME

FAQSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

FAQSchema['title'].storage = atapi.AnnotationStorage()
FAQSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(FAQSchema, moveDiscussion=False)


class FAQ(base.ATCTContent):
    """A content type for the frequently asked questions"""
    implements(IFAQ)

    meta_type = "FAQ"
    schema = FAQSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(FAQ, PROJECTNAME)
