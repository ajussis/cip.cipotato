"""Definition of the Personnel Container content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import IPersonnelContainer
from cip.ciptypes.config import PROJECTNAME

PersonnelContainerSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

PersonnelContainerSchema['title'].storage = atapi.AnnotationStorage()
PersonnelContainerSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    PersonnelContainerSchema,
    folderish=True,
    moveDiscussion=False
)


class PersonnelContainer(folder.ATFolder):
    """Container for Person content types"""
    implements(IPersonnelContainer)

    meta_type = "PersonnelContainer"
    schema = PersonnelContainerSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(PersonnelContainer, PROJECTNAME)
