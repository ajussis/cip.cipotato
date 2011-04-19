from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime

class PublicationsView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/publications.pt')

    def Pubs(self, address):
#        import pdb; pdb.set_trace()
        pubpath = (self.context.portal_url.getPortalPath()+'/resources/publications/'+address)
        return self.context.portal_catalog.searchResults(path = {"query": (pubpath)},portal_type="Publication", sort_on="Date", sort_order="reverse")[:1]

    def ImageExist(self, img_id):
#        import pdb; pdb.set_trace()
        img_id = img_id + '-jpg'
        img = self.context.portal_catalog.searchResults(id=img_id)
        if img:
            return img_id
        else:
            return 0

class PublicationsSubView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/publications_sub.pt')

    def Pubs(self, address):
#        import pdb; pdb.set_trace()
        pubpath = (self.context.portal_url.getPortalPath()+'/resources/publications/'+address)
        return self.context.portal_catalog.searchResults(path = {"query": (pubpath)},portal_type="Publication", sort_on="Date", sort_order="reverse")[:2]

    def ImageExist(self, img_id):
#        import pdb; pdb.set_trace()
        img_id = img_id + '-jpg'
        img = self.context.portal_catalog.searchResults(id=img_id)
        if img:
            return img_id
        else:
            return 0

class PublicationsOneView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/publications_one.pt')

    def Pubs(self, address):
#        import pdb; pdb.set_trace()
        pubpath = (self.context.portal_url.getPortalPath()+'/resources/publications/'+address)
        return self.context.portal_catalog.searchResults(path = {"query": (pubpath)},portal_type="Publication", sort_on="Date", sort_order="reverse")[:2]

    def ImageExist(self, img_id):
#        import pdb; pdb.set_trace()
        img_id = img_id + '-jpg'
        img = self.context.portal_catalog.searchResults(id=img_id)
        if img:
            return img_id
        else:
            return 0