from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.ciptypes import ciptypesMessageFactory as _



class IFAQ(Interface):
    """A content type for the frequently asked questions"""

    # -*- schema definition goes here -*-
    answer = schema.TextLine(
        title=_(u"Answer"),
        required=False,
        description=_(u"Answer"),
    )
#
