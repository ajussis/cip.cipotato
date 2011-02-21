"""Definition of the Pubholder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import IPubholder
from cip.ciptypes.config import PROJECTNAME

PubholderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

PubholderSchema['title'].storage = atapi.AnnotationStorage()
PubholderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    PubholderSchema,
    folderish=True,
    moveDiscussion=False
)


class Pubholder(folder.ATFolder):
    """Folder for publications"""
    implements(IPubholder)

    meta_type = "Pubholder"
    schema = PubholderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Pubholder, PROJECTNAME)
