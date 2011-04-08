from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.ciptypes import ciptypesMessageFactory as _



class ISeminar(Interface):
    """A content type for the seminars to include videos, flash, documents anaudio"""

    # -*- schema definition goes here -*-
    place = schema.TextLine(
        title=_(u"Place"),
        required=False,
        description=_(u"Where the seminar is held"),
    )
#
    seminardate = schema.Date(
        title=_(u"Date of seminar"),
        required=False,
        description=_(u"Add the date when the seminar is being held"),
    )
#
    image = schema.Bytes(
        title=_(u"Seminar image"),
        required=False,
        description=_(u"Add a representative image of the seminar"),
    )
#
    audio = schema.TextLine(
        title=_(u"Audio"),
        required=False,
        description=_(u"Audio"),
    )
#
    presentation = schema.TextLine(
        title=_(u"Presentation"),
        required=False,
        description=_(u"Presentation"),
    )
#
    abstract = schema.TextLine(
        title=_(u"Abstract"),
        required=False,
        description=_(u"Abstract"),
    )
#
    biography = schema.TextLine(
        title=_(u"Biography"),
        required=False,
        description=_(u"Biography"),
    )
#
    speaker = schema.TextLine(
        title=_(u"Speaker"),
        required=False,
        description=_(u"Speaker"),
    )
#
