from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.ciptypes import ciptypesMessageFactory as _



class IPerson(Interface):
    """Content type for personnel listings"""

    # -*- schema definition goes here -*-
    section = schema.TextLine(
        title=_(u"Section"),
        required=False,
        description=_(u"Add section"),
    )
#
    head = schema.Bool(
        title=_(u"Head"),
        required=False,
        description=_(u"Check if head of department"),
    )
#
    elsewhere = schema.TextLine(
        title=_(u"Elsewhere"),
        required=False,
        description=_(u"Elsewhere on the web"),
    )
#
    publications = schema.TextLine(
        title=_(u"Publications"),
        required=False,
        description=_(u"Publications"),
    )
#
    languages = schema.TextLine(
        title=_(u"Languages"),
        required=False,
        description=_(u"Languages"),
    )
#
    skype = schema.TextLine(
        title=_(u"Skype"),
        required=False,
        description=_(u"Skype"),
    )
#
    tel = schema.TextLine(
        title=_(u"Telephone"),
        required=False,
        description=_(u"Telephone"),
    )
#
    areas = schema.TextLine(
        title=_(u"Areas"),
        required=False,
        description=_(u"Areas"),
    )
#
    subsection = schema.TextLine(
        title=_(u"Subsection"),
        required=False,
        description=_(u"Subsection"),
    )
#
    bio = schema.Text(
        title=_(u"Bio"),
        required=False,
        description=_(u"Biography of the person"),
    )
#
    country = schema.TextLine(
        title=_(u"Country"),
        required=False,
        description=_(u"Country"),
    )
#
    email = schema.TextLine(
        title=_(u"Email"),
        required=False,
        description=_(u"Email address of the person"),
    )
#
    position = schema.TextLine(
        title=_(u"Position"),
        required=False,
        description=_(u"Add position of the person"),
    )
#
    lastname = schema.TextLine(
        title=_(u"Last name"),
        required=True,
        description=_(u"Add last names"),
    )
#
    firstname = schema.TextLine(
        title=_(u"First name"),
        required=True,
        description=_(u"Add first names"),
    )
#
