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
        """
        from transaction import commit
        import pdb; pdb.set_trace()
        brains = self.context.portal_catalog(path={"query" : "/cipotato/publications/pdf"})
        for i in brains:
            try:
                "-" in i.id
                c = i.getObject()
                parent = c.aq_parent
                parent.manage_renameObject(i.id, (i.id).replace("-","."))
                commit()
                print i.id + " changed to .pdf!"
            except:
                print i.id + " doesn't have '-', maybe it has been changed already"
                continue
            #m = m.replace("-", ".")
            #m.manage_renameObject(id, id+"ii")
        return results"""

    def scholarinfo(self):
        results = self.context.portal_catalog.searchResults(path={"query" : "/cipotato/about-cip/jobs/open-scholarships/"}, portal_type="Career")
        return results
