# -*- coding: utf-8 -*-
"""Use collective.transmogrifier to import Persons."""

from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from collective.transmogrifier.transmogrifier import Transmogrifier

class ImportView(BrowserView):

    def __call__(self):    

        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        portal = portal_state.portal()
        
        transmogrifier = Transmogrifier(portal)
        transmogrifier('News import')

        return 'Import done.'

