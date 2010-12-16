"""Definition of the Gallery content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import IGallery
from cip.ciptypes.config import PROJECTNAME

GallerySchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

GallerySchema['title'].storage = atapi.AnnotationStorage()
GallerySchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    GallerySchema,
    folderish=True,
    moveDiscussion=False
)


class Gallery(folder.ATFolder):
    """A content type for galleries"""
    implements(IGallery)

    meta_type = "Gallery"
    schema = GallerySchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Gallery, PROJECTNAME)
