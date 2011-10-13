from Products.CMFCore.utils import getToolByName
import transaction
from Products.Five.browser import BrowserView

class Changepubs(BrowserView):
    portal = app.cipotato
    catalog = getToolByName(portal, 'portal_catalog')
    docs = catalog(path={"query":"/cipotato/publications/pdf"})
    pdfs = catalog(Type="Publication")
    import pdb;pdb.set_trace()
    transaction.begin()
    for i in docs:
        did = i.Title.split(".")[0]
        try:
            print i.Title+" changed to "
            i.Title = catalog.searchResults(getPubcode=did)[0].Title
            print i.Title
        except:
            continue

    import transaction
    transaction.commit()
    #app._p_jar.sync()
