"""Definition of the Seminar content type
"""

from zope.interface import implements
from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from plone.app.blob.field import BlobField, ImageField
from Products.CMFCore.permissions import View

# -*- Message Factory Imported Here -*-
from cip.ciptypes import ciptypesMessageFactory as _

from cip.ciptypes.interfaces import ISeminar
from cip.ciptypes.config import PROJECTNAME

SeminarSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.DateTimeField(
        'seminardate',
        storage=atapi.AnnotationStorage(),
        required=1,
        widget=atapi.CalendarWidget(
            label=_(u"Date of seminar"),
            description=_(u"Add the date when the seminar is being held"),
        ),
        validators=('isValidDate'),
    ),

    atapi.ImageField(
        'image',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Seminar image"),
            description=_(u"Add a representative image of the seminar"),
        ),
    ),

    BlobField(
        'audio',
        widget=atapi.FileWidget(
            label=_(u"Audio"),
            description=_(u"Audio"),
        ),
    ),

    BlobField(
        'presentation',
        widget=atapi.FileWidget(
            label=_(u"Presentation"),
            description=_(u"Presentation"),
        ),
    ),


    BlobField(
        'abstract',
        widget=atapi.FileWidget(
            label=_(u"Abstract"),
            description=_(u"Abstract"),
        ),
    ),


    BlobField(
        'biography',
        widget=atapi.FileWidget(
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

    image = atapi.ATFieldProperty('image')

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    seminardate = atapi.ATFieldProperty('seminardate')

    speaker = atapi.ATFieldProperty('speaker')


atapi.registerType(Seminar, PROJECTNAME)
