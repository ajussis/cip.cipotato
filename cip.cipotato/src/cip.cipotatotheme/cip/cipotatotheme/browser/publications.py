from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime
from zope.interface import implements, Interface
from zope import schema

from Products.ATContentTypes.interface import IATTopic

#from cip.cipotatotheme import appMessageFactory as _


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


class IPublicationsSubView(Interface):
    """ Allowed template variables exposed from the view.
    """

    # Item list as iterable Products.CMFPlone.PloneBatch.Batch object
    contents = schema.Object(Interface)



class PublicationsSubView(BrowserView):
    """
    List summary information for all publications in the folder.
    Batch results.
    """
    #__call__ = ViewPageTemplateFile('templates/publications_sub.pt')

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

    implements(IPublicationsSubView)

    def query(self, start, limit, contentFilter):
        """ Make catalog query for the folder listing.

        @param start: First index to query

        @param limit: maximum number of items in the batch

        @param contentFilter: portal_catalog filtering dictionary with index -> value pairs.

        @return: Products.CMFPlone.PloneBatch.Batch object
        """

        # Batch size
        b_size = limit

        # Batch start index, zero based
        b_start = start

        # We use different query method, depending on
        # whether we do listing for topic or folder
        if IATTopic.providedBy(self.context):
            # ATTopic like content
            # Call Products.ATContentTypes.content.topic.ATTopic.queryCatalog() method
            # This method handles b_start internally and
            # grabs it from HTTPRequest object
            return self.context.queryCatalog(contentFilter, batch=True, b_size=b_size)
        else:
            # Folder or Large Folder like content
            # Call CMFPlone(/skins/plone_scripts/getFolderContents Python script
            # This method handles b_start parametr internally and grabs it from the request object
            contentFilter['sort_order'] = "descending"
            return self.context.getFolderContents(contentFilter, batch=True, b_size=b_size)

    def __call__(self):
        """ Render the content item listing.
        """
        limit = 10
        filter = { "portal_type" : "Publication" }
        # Read the first index of the selected batch parameter as HTTP GET request query parameter
        start = self.request.get("b_start", 0)
        # Perform portal_catalog query
        self.contents = self.query(start, limit, filter)
        # Return the rendered template (productcardsummaryview.pt), with content listing information filled in
        return self.index()


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