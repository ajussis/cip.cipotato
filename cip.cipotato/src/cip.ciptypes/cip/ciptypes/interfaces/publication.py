from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.ciptypes import ciptypesMessageFactory as _



class IPublication(Interface):
    """CIP Publication"""

    # -*- schema definition goes here -*-
    type = schema.TextLine(
        title=_(u"Publication type"),
        required=False,
        description=_(u"Add the type of the publication (book, working paper)"),
    )
#
    coverimage = schema.Bytes(
        title=_(u"Cover Image"),
        required=False,
        description=_(u"Insert the publication's cover image"),
    )
#
