from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime
import DateTime, time

class JobsView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/jobs.pt')

    def jobinfo(self):
        now = DateTime.DateTime()
        i = self.context.portal_catalog.searchResults(path={"query" : "/".join(self.context.getPhysicalPath())}, portal_type="Career")
        openjobs = []
        for joo in i:
            m = joo.getObject()
            jobdate = m.getJobdate()
            if (now < jobdate):
                openjobs.append(joo)
        return openjobs

class JobsOpenView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/jobsopen.pt')

    def jobinfo(self):
        #import pdb; pdb.set_trace()
        now = DateTime.DateTime()
        i = self.context.portal_catalog.searchResults(path={"query" : "/".join(self.context.getPhysicalPath())}, portal_type="Career")
        openjobs = []
        for joo in i:
            m = joo.getObject()
            jobdate = m.getJobdate()
            if (now < jobdate):
                openjobs.append(joo)
        return openjobs