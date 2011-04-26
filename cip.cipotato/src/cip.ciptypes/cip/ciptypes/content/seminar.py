"""Definition of the Seminar content type
"""

from zope.interface import implements
from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from plone.app.blob.field import BlobField, ImageField
from Products.CMFCore.permissions import View
from AccessControl import ClassSecurityInfo

# -*- Message Factory Imported Here -*-
from cip.ciptypes import ciptypesMessageFactory as _

from cip.ciptypes.interfaces import ISeminar
from cip.ciptypes.config import PROJECTNAME

SeminarSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-


    atapi.StringField(
        'speaker',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Speaker"),
            description=_(u"Speaker"),
        ),
    ),

    atapi.StringField(
        'speakerinstitution',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Speaker's organization"),
            description=_(u"Add the organization the speaker's from"),
        ),
    ),

    atapi.StringField(
        'place',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Place"),
            description=_(u"Where the seminar is held"),
        ),
    ),


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
        sizes= {'preview' : (400, 400),
                'mini'    : (200, 200),
                'thumb'   : (128, 128),
                'tile'    :  (64, 64),
                'icon'    :  (32, 32),
                'listing' :  (16, 16),
          },
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
        index="FieldIndex:schema",
        index_method="hasAudio",
    ),

    BlobField(
        'presentation',
        widget=atapi.FileWidget(
            label=_(u"Presentation"),
            description=_(u"Presentation"),
        ),
        index="FieldIndex:schema",
        index_method="hasPresentation",
    ),

    atapi.StringField(
        'presentationurl',
        validators = ('isURL',),
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Presentation's URL"),
            description=_(u"In case the presentation is hosted for example in Google Docs, add the url here"),
        ),
    ),

    BlobField(
        'abstract',
        widget=atapi.FileWidget(
            label=_(u"Abstract"),
            description=_(u"Abstract"),
        ),
        index="FieldIndex:schema",
        index_method="hasAbstract",
    ),


    BlobField(
        'biography',
        widget=atapi.FileWidget(
            label=_(u"Biography"),
            description=_(u"Biography"),
        ),
        index="FieldIndex:schema",
        index_method="hasBiography",
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
    presentationurl = atapi.ATFieldProperty('presentationurl')

    speakerinstitution = atapi.ATFieldProperty('speakerinstitution')

    place = atapi.ATFieldProperty('place')

    seminardate = atapi.ATFieldProperty('seminardate')

    speaker = atapi.ATFieldProperty('speaker')

    security = ClassSecurityInfo()
    
    security.declarePublic('hasAudio')
    def hasAudio(self):
        """This method returns true or false depending on whether the object has this field for the catalog"""

        result = 0
        if (len(self['audio']) != 0):
            result = 1
        return result

    security.declarePublic('hasPresentation')
    def hasPresentation(self):
        """This method returns true or false depending on whether the object has this field for the catalog"""

        result = 0
        if (len(self['presentation']) != 0):
            result = 1
        return result

    security.declarePublic('hasBiography')
    def hasBiography(self):
        """This method returns true or false depending on whether the object has this field for the catalog"""

        result = 0
        if (len(self['biography']) != 0):
            result = 1
        return result

    security.declarePublic('hasAbstract')
    def hasAbstract(self):
        """This method returns true or false depending on whether the object has this field for the catalog"""

        result = 0
        if (len(self['abstract']) != 0):
            result = 1
        return result

    security.declarePublic('hasPresentationurl')
    def hasPresentationurl(self):
        """This method returns true or false depending on whether the object has this field for the catalog"""

        result = 0
        if (len(self['presentationurl']) != 0):
            result = 1
        return result


atapi.registerType(Seminar, PROJECTNAME)
