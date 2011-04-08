from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime

class SeminarsyearView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/seminarsyear.pt')

    def getYear(self):
        return (self.request.get('URL')).rsplit('/',2)[1]

    def seminars(self):
        #import pdb; pdb.set_trace()
        url = '/'.join(self.context.getPhysicalPath())
        results = self.context.portal_catalog.searchResults(path={'query':url}, portal_type="Seminar")
        print results
        return results