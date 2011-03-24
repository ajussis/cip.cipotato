from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime

class SeminarsmainView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/seminarsmain.pt')

    def seminars(self):
        results = self.context.portal_catalog.searchResults(path={"query" : "/cipotato/resources/capacity-strengthening/seminars/seminars-archive"}, portal_type="Seminar")
        return results