from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime

class ContactsView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/contacts.pt')

    def cpad(self,subsection):
        results = self.context.portal_catalog.searchResults(portal_type="Person", getSubsection=subsection)
        return results

    def cpadHead(self,subsection):
        #import pdb; pdb.set_trace()
        result = self.context.portal_catalog.searchResults(portal_type="Person", getSubsection=subsection, getHead=1)
        if (result):
            return result[0]
        else:
            return 0

    def dg(self):
        """
        Get all the persons working for CPAD
        """
        results = self.context.portal_catalog.searchResults(portal_type="Person", getSubsection="DG")
        return results

    def grants(self):
        """
        Get all the persons working for CPAD
        """
        #import ipdb
        #ipdb.set_trace()
        results = self.context.portal_catalog.searchResults(portal_type="Person", getSubsection="Grants")
        return results
