"""Definition of the Person content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.ciptypes import ciptypesMessageFactory as _

from cip.ciptypes.interfaces import IPerson
from cip.ciptypes.config import PROJECTNAME

PersonSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'section',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Section"),
            description=_(u"Add section"),
        ),
    ),


    atapi.BooleanField(
        'head',
        storage=atapi.AnnotationStorage(),
        widget=atapi.BooleanWidget(
            label=_(u"Head"),
            description=_(u"Check if head of department"),
        ),
    ),


    atapi.StringField(
        'elsewhere',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Elsewhere"),
            description=_(u"Elsewhere on the web"),
        ),
    ),


    atapi.StringField(
        'publications',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Publications"),
            description=_(u"Publications"),
        ),
    ),


    atapi.StringField(
        'languages',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Languages"),
            description=_(u"Languages"),
        ),
    ),


    atapi.StringField(
        'skype',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Skype"),
            description=_(u"Skype"),
        ),
    ),


    atapi.StringField(
        'tel',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Telephone"),
            description=_(u"Telephone"),
        ),
    ),


    atapi.StringField(
        'areas',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Areas"),
            description=_(u"Areas"),
        ),
    ),


    atapi.StringField(
        'subsection',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Subsection"),
            description=_(u"Add subsection"),
        ),
    ),


    atapi.TextField(
        'bio',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Bio"),
            description=_(u"Biography of the person"),
        ),
    ),


    atapi.StringField(
        'country',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Country"),
            description=_(u"Country"),
        ),
    ),


    atapi.StringField(
        'email',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Email"),
            description=_(u"Email address of the person"),
        ),
    ),


    atapi.StringField(
        'position',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Position"),
            description=_(u"Add position of the person"),
        ),
    ),


    atapi.StringField(
        'lastname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Last name"),
            description=_(u"Add last names"),
        ),
        required=True,
    ),


    atapi.StringField(
        'firstname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"First name"),
            description=_(u"Add first names"),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PersonSchema['title'].storage = atapi.AnnotationStorage()
PersonSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(PersonSchema, moveDiscussion=False)


class Person(base.ATCTContent):
    """Content type for personnel listings"""
    implements(IPerson)

    meta_type = "Person"
    schema = PersonSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    section = atapi.ATFieldProperty('section')

    head = atapi.ATFieldProperty('head')

    elsewhere = atapi.ATFieldProperty('elsewhere')

    publications = atapi.ATFieldProperty('publications')

    languages = atapi.ATFieldProperty('languages')

    skype = atapi.ATFieldProperty('skype')

    tel = atapi.ATFieldProperty('tel')

    areas = atapi.ATFieldProperty('areas')

    subsection = atapi.ATFieldProperty('subsection')

    bio = atapi.ATFieldProperty('bio')

    country = atapi.ATFieldProperty('country')

    email = atapi.ATFieldProperty('email')

    position = atapi.ATFieldProperty('position')

    lastname = atapi.ATFieldProperty('lastname')

    firstname = atapi.ATFieldProperty('firstname')


atapi.registerType(Person, PROJECTNAME)
