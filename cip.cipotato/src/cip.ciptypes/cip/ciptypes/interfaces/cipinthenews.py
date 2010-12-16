from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.ciptypes import ciptypesMessageFactory as _



class ICIPintheNews(Interface):
    """A content type to add external media articles"""

    # -*- schema definition goes here -*-
    newsurl = schema.TextLine(
        title=_(u"URL"),
        required=True,
        description=_(u"URL address for the news item"),
    )
#
    pubdate = schema.Date(
        title=_(u"Publication date"),
        required=True,
        description=_(u"The date when the news was originally published"),
    )
#
    mediasource = schema.TextLine(
        title=_(u"Media source"),
        required=True,
        description=_(u"Add the name of the media organization"),
    )
#
