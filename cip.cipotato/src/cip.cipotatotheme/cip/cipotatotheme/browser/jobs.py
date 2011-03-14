from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime

class JobsView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/jobs.pt')

    def jobinfo(self):
        results = self.context.portal_catalog.searchResults(path={"query" : "/cipotato/about-cip/jobs/open-positions/"}, portal_type="Career")
        
        #import pdb; pdb.set_trace()
        return results

    def scholarinfo(self):
        results = self.context.portal_catalog.searchResults(path={"query" : "/cipotato/about-cip/jobs/open-scholarships/"}, portal_type="Career")
        return results
