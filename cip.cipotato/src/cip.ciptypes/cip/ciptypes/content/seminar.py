"""Definition of the Seminar content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.ciptypes import ciptypesMessageFactory as _

from cip.ciptypes.interfaces import ISeminar
from cip.ciptypes.config import PROJECTNAME

SeminarSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'audio',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Audio"),
            description=_(u"Audio"),
        ),
    ),


    atapi.StringField(
        'presentation',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Presentation"),
            description=_(u"Presentation"),
        ),
    ),


    atapi.StringField(
        'abstract',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Abstract"),
            description=_(u"Abstract"),
        ),
    ),


    atapi.StringField(
        'biography',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Biography"),
            description=_(u"Biography"),
        ),
    ),


    atapi.StringField(
        'speaker',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Speaker"),
            description=_(u"Speaker"),
        ),
    ),


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
    audio = atapi.ATFieldProperty('audio')

    presentation = atapi.ATFieldProperty('presentation')

    abstract = atapi.ATFieldProperty('abstract')

    biography = atapi.ATFieldProperty('biography')

    speaker = atapi.ATFieldProperty('speaker')


atapi.registerType(Seminar, PROJECTNAME)
