"""Definition of the Jobs content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.ciptypes import ciptypesMessageFactory as _

from cip.ciptypes.interfaces import IJobs
from cip.ciptypes.config import PROJECTNAME

JobsSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'body',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Job description"),
            description=_(u"Add the full description of the job"),
        ),
    ),


    atapi.DateTimeField(
        'jobsdate',
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

JobsSchema['title'].storage = atapi.AnnotationStorage()
JobsSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(JobsSchema, moveDiscussion=False)


class Jobs(base.ATCTContent):
    """Open jobs and traineeships at CIP"""
    implements(IJobs)

    meta_type = "Jobs"
    schema = JobsSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    body = atapi.ATFieldProperty('body')

    jobsdate = atapi.ATFieldProperty('jobsdate')

    type = atapi.ATFieldProperty('type')

    unit = atapi.ATFieldProperty('unit')


atapi.registerType(Jobs, PROJECTNAME)
