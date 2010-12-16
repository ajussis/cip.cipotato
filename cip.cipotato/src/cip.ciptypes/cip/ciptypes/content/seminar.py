"""Definition of the Seminar content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import ISeminar
from cip.ciptypes.config import PROJECTNAME

SeminarSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

SeminarSchema['title'].storage = atapi.AnnotationStorage()
SeminarSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    SeminarSchema,
    folderish=True,
    moveDiscussion=False
)


class Seminar(folder.ATFolder):
    """A content type for the seminars to include videos, flash, documents anaudio"""
    implements(ISeminar)

    meta_type = "Seminar"
    schema = SeminarSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Seminar, PROJECTNAME)
