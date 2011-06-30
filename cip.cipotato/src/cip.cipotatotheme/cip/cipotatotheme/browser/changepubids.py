from Products.CMFCore.utils import getToolByName
import transaction
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Changepubs(BrowserView):

    __call__ = ViewPageTemplateFile('changepubs.pt')

    def changepubtitles(self):
        docs = self.context.portal_catalog(path={"query":"/cipotato/publications/pdf"})[:4]
        #pdfs = self.context.portal_catalog(Type="Publication")
        import pdb;pdb.set_trace()
        transaction.begin()
        for i in docs:
            did = i.Title.split(".")[0]
            iob = i.getObject()
            try:
                print i.Title+" changed to "
                iob.setTitle(self.context.portal_catalog.searchResults(getPubcode=did)[0].Title)
                iob.reindexObject()
                print iob.Title()
            except:
                continue
        transaction.commit()
        #app._p_jar.sync()
