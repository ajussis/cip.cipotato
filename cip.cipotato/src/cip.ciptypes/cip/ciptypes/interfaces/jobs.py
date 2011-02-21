from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.ciptypes import ciptypesMessageFactory as _



class IJobs(Interface):
    """Open jobs and traineeships at CIP"""

    # -*- schema definition goes here -*-
    body = schema.SourceText(
        title=_(u"Job description"),
        required=False,
        description=_(u"Add the full description of the job"),
    )
#
    date = schema.Date(
        title=_(u"Date"),
        required=False,
        description=_(u"Ending date for applying"),
    )
#
    type = schema.TextLine(
        title=_(u"Type of Vacancy"),
        required=False,
        description=_(u"Type of Vacancy"),
    )
#
    unit = schema.TextLine(
        title=_(u"Organizational unit"),
        required=False,
        description=_(u"Add the code for organizational unit"),
    )
#
