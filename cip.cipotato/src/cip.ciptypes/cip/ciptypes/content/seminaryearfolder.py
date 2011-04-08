"""Definition of the Seminar Year Folder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import ISeminarYearFolder
from cip.ciptypes.config import PROJECTNAME

SeminarYearFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

SeminarYearFolderSchema['title'].storage = atapi.AnnotationStorage()
SeminarYearFolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    SeminarYearFolderSchema,
    folderish=True,
    moveDiscussion=False
)


class SeminarYearFolder(folder.ATFolder):
    """This content type can include seminars. Create one for each year"""
    implements(ISeminarYearFolder)

    meta_type = "SeminarYearFolder"
    schema = SeminarYearFolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(SeminarYearFolder, PROJECTNAME)
