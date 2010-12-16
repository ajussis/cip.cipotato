"""Definition of the Career content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import ICareer
from cip.ciptypes.config import PROJECTNAME

CareerSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CareerSchema['title'].storage = atapi.AnnotationStorage()
CareerSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CareerSchema, moveDiscussion=False)


class Career(base.ATCTContent):
    """A content type for the jobs and scholarships"""
    implements(ICareer)

    meta_type = "Career"
    schema = CareerSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Career, PROJECTNAME)
