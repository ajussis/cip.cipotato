"""Definition of the Career content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.ciptypes.interfaces import ICareer
from cip.ciptypes.config import PROJECTNAME

from cip.ciptypes import ciptypesMessageFactory as _

CareerSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'body',
        default_output_type = 'text/x-html-safe',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Job description"),
            description=_(u"Add the full description of the job"),
        ),
    ),


    atapi.DateTimeField(
        'jobdate',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Date"),
            description=_(u"Ending date for applying"),
        ),
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'type',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Type of Vacancy"),
            description=_(u"Type of Vacancy"),
        ),
    ),


    atapi.StringField(
        'unit',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Organizational unit"),
            description=_(u"Add the code for organizational unit"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

CareerSchema['title'].storage = atapi.AnnotationStorage()
CareerSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(CareerSchema, moveDiscussion=False)


class Career(base.ATCTContent):
    """A content type for the jobs and scholarships"""
    implements(ICareer)

    meta_type = "Career"
    schema = CareerSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    body = atapi.ATFieldProperty('body')

    jobdate = atapi.ATFieldProperty('jobdate')

    type = atapi.ATFieldProperty('type')

    unit = atapi.ATFieldProperty('unit')


atapi.registerType(Career, PROJECTNAME)
