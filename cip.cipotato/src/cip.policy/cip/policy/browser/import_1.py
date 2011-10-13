# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter

class ImportView(BrowserView):

    def __call__(self):

        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        portal = portal_state.portal()

