from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.ciptypes import ciptypesMessageFactory as _



class IPublication(Interface):
    """CIP Publication"""

    # -*- schema definition goes here -*-
    author = schema.TextLine(
        title=_(u"Author"),
        required=False,
        description=_(u"Author"),
    )
#
    pub_abstract = schema.TextLine(
        title=_(u"Pub_Abstract"),
        required=False,
        description=_(u"Pub_Abstract"),
    )
#
    pub_salenote = schema.TextLine(
        title=_(u"Pub_SaleNote"),
        required=False,
        description=_(u"Pub_SaleNote"),
    )
#
    pubstock = schema.TextLine(
        title=_(u"PubStock"),
        required=False,
        description=_(u"PubStock"),
    )
#
    pub_earthprint = schema.TextLine(
        title=_(u"Pub_EarthPrint"),
        required=False,
        description=_(u"Pub_EarthPrint"),
    )
#
    pubcode = schema.TextLine(
        title=_(u"PubCode"),
        required=False,
        description=_(u"PubCode"),
    )
#
    pdf = schema.TextLine(
        title=_(u"PDF"),
        required=False,
        description=_(u"PDF"),
    )
#
    image = schema.TextLine(
        title=_(u"Image"),
        required=False,
        description=_(u"Image"),
    )
#
    link = schema.TextLine(
        title=_(u"Link"),
        required=False,
        description=_(u"Link"),
    )
#
    price = schema.TextLine(
        title=_(u"Price"),
        required=False,
        description=_(u"Price"),
    )
#
    pages = schema.TextLine(
        title=_(u"Pages"),
        required=False,
        description=_(u"Pages"),
    )
#
    issn = schema.TextLine(
        title=_(u"ISSN"),
        required=False,
        description=_(u"ISSN"),
    )
#
    isbn = schema.TextLine(
        title=_(u"ISBN"),
        required=False,
        description=_(u"ISBN"),
    )
#
    publisher = schema.TextLine(
        title=_(u"Publisher"),
        required=False,
        description=_(u"Publisher"),
    )
#
    imprint = schema.TextLine(
        title=_(u"Imprint"),
        required=False,
        description=_(u"Imprint"),
    )
#
    division = schema.TextLine(
        title=_(u"Division"),
        required=False,
        description=_(u"Division"),
    )
#
    category = schema.TextLine(
        title=_(u"Category"),
        required=False,
        description=_(u"Category"),
    )
#
    year = schema.TextLine(
        title=_(u"Year"),
        required=False,
        description=_(u"Year"),
    )
#
    conference = schema.TextLine(
        title=_(u"Conference"),
        required=False,
        description=_(u"Conference"),
    )
#
    series = schema.TextLine(
        title=_(u"Series"),
        required=False,
        description=_(u"Series"),
    )
#

