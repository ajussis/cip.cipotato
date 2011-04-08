from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime

class SeminarsarchiveView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/seminarsarchive.pt')

    def getSeminarsyear(self, year):
        yeardict = {}
        resultsfinal = []
        #import pdb; pdb.set_trace()
        results = self.context.portal_catalog.searchResults(path={"query" : "/cipotato/resources/capacity-strengthening/seminars/seminars-archive"}, portal_type="Seminar", sort_on="Date")
        for i in results:
            yearobj = i.getObject().getSeminardate()
            print 'yobj: ', yearobj, 'year: ', year
            if (str(yearobj).split('/')[0] == year):
                resultsfinal.append(i)
                print resultsfinal
        return resultsfinal

    def getYear(self):
        return str(datetime.now())[:4]

"""        import pdb; pdb.set_trace()
        for i in results:
            try:
                date = i.getObject().getSeminardate()
                year = str(date).split("/")[0]
                yeardict[year] = years.append[i]
            except:
                continue
        count = 0
        for i in yeardict:
            finalresults.append(i)
"""