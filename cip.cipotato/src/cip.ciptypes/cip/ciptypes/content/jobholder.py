"""Definition of the Jobholder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import IJobholder
from cip.ciptypes.config import PROJECTNAME

JobholderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

JobholderSchema['title'].storage = atapi.AnnotationStorage()
JobholderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    JobholderSchema,
    folderish=True,
    moveDiscussion=False
)


class Jobholder(folder.ATFolder):
    """Folder for jobs"""
    implements(IJobholder)

    meta_type = "Jobholder"
    schema = JobholderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Jobholder, PROJECTNAME)
