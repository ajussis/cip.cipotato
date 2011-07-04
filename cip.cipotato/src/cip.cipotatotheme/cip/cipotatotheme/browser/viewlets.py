from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from datetime import date
from Acquisition import aq_base, aq_inner
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from plone.memoize.view import memoize
from urllib import unquote
from plone.app.layout.viewlets import common
from plone.app.layout.globals.interfaces import IViewView
from zope.interface import implements, alsoProvides
from zope.viewlet.interfaces import IViewlet
from Products.CMFPlone.utils import base_hasattr
from datetime import datetime
from Products.Five.browser import BrowserView
from plone.app.layout.viewlets.common import SearchBoxViewlet
import DateTime

# Sample code for a basic viewlet (In order to use it, you'll have to):
# - Un-comment the following useable piece of code (viewlet python class).
# - Rename the viewlet template file ('browser/viewlet.pt') and edit the
#   following python code accordingly.
# - Edit the class and template to make them suit your needs.
# - Make sure your viewlet is correctly registered in 'browser/configure.zcml'.
# - If you need it to appear in a specific order inside its viewlet manager,
#   edit 'profiles/default/viewlets.xml' accordingly.
# - Restart Zope.
# - If you edited any file in 'profiles/default/', reinstall your package.
# - Once you're happy with your viewlet implementation, remove any related
#   (unwanted) inline documentation  ;-p

#class MyViewlet(ViewletBase):
#    render = ViewPageTemplateFile('viewlet.pt')
#
#    def update(self):
#        self.computed_value = 'any output'


class FooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/footer.pt')

    def update(self):
        self.year = date.today().year

class ContentViewsViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/contentviews.pt')

    @memoize
    def prepareObjectTabs(self, default_tab='view', sort_first=['folderContents']):
        """Prepare the object tabs by determining their order and working
        out which tab is selected. Used in global_contentviews.pt
        """
        context = aq_inner(self.context)
        context_url = context.absolute_url()
        context_fti = context.getTypeInfo()

        context_state = getMultiAdapter(
            (context, self.request), name=u'plone_context_state'
        )
        actions = context_state.actions

        action_list = []
        if context_state.is_structural_folder():
            action_list = actions('folder')
        action_list.extend(actions('object'))

        tabs = []
        found_selected = False
        fallback_action = None

        request_url = self.request['ACTUAL_URL']
        request_url_path = request_url[len(context_url):]

        if request_url_path.startswith('/'):
            request_url_path = request_url_path[1:]
        for action in action_list:
            item = {'title'    : action['title'],
                    'id'       : action['id'],
                    'url'      : '',
                    'selected' : False}

            action_url = action['url'].strip()
            starts = action_url.startswith
            if starts('http') or starts('javascript'):
                item['url'] = action_url
            else:
                item['url'] = '%s/%s' % (context_url, action_url)

            action_method = item['url'].split('/')[-1]

            # Action method may be a method alias:
            # Attempt to resolve to a template.
            action_method = context_fti.queryMethodID(
                action_method, default=action_method
            )
            if action_method:
                request_action = unquote(request_url_path)
                request_action = context_fti.queryMethodID(
                    request_action, default=request_action
                )
                if action_method == request_action:
                    item['selected'] = True
                    found_selected = True

            current_id = item['id']
            if current_id == default_tab:
                fallback_action = item

            tabs.append(item)

        if not found_selected and fallback_action is not None:
            fallback_action['selected'] = True

        def sortOrder(tab):
            try:
                return sort_first.index(tab['id'])
            except ValueError:
                return 255

        tabs.sort(key=sortOrder)
        return tabs

class PathBarViewlet(common.PathBarViewlet):
    render = ViewPageTemplateFile('templates/path_bar.pt')

class ContentActionsViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/contentactions.pt')

    def update(self):
        context = aq_inner(self.context)
        context_state = getMultiAdapter((context, self.request),
                                        name=u'plone_context_state')

        self.object_actions = context_state.actions('object_actions')

        # The drop-down menus are pulled in via a simple content provider
        # from plone.app.contentmenu. This behaves differently depending on
        # whether the view is marked with IViewView. If our parent view
        # provides that marker, we should do it here as well.
        if IViewView.providedBy(self.__parent__):
            alsoProvides(self, IViewView)

    def icon(self, action):
        return action.get('icon', None)

class SearchBoxViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/searchbox.pt')

    def update(self):
        super(SearchBoxViewlet, self).update()

        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')

        props = getToolByName(self.context, 'portal_properties')
        livesearch = props.site_properties.getProperty('enable_livesearch', False)
        if livesearch:
            self.search_input_id = "searchGadget"
        else:
            self.search_input_id = "nolivesearchGadget" # don't use "" here!

        folder = context_state.folder()
        self.folder_path = '/'.join(folder.getPhysicalPath())


class GalleryView(BrowserView):
    __call__ = ViewPageTemplateFile('templates/galleryview.pt')

    def getGalleries(self):
        results = self.context.portal_catalog.searchResults(path={"query" : (self.context.portal_url.getPortalPath()+"/press-room/photo-gallery/general")}, sort_order="ascending")
        #import pdb;pdb.set_trace()
        return results

    def getEventGalleries(self):
        results = self.context.portal_catalog.searchResults(path={"query" : (self.context.portal_url.getPortalPath()+"/press-room/photo-gallery/events")}, sort_order="ascending", portal_type="Gallery")
        return results

#testing searchboxes
class SearchBoxPubViewlet(SearchBoxViewlet):
    render = ViewPageTemplateFile("templates/searchboxpub.pt")


class ContentRelatedItems(ViewletBase):

    index = ViewPageTemplateFile("templates/document_relateditems.pt")

    def related_items(self):
        context = aq_inner(self.context)
        res = ()
        if base_hasattr(context, 'getRawRelatedItems'):
            catalog = getToolByName(context, 'portal_catalog')
            related = context.getRawRelatedItems()
            if not related:
                return ()
            brains = catalog(UID=related)
            if brains:
                # build a position dict by iterating over the items once
                positions = dict([(v, i) for (i, v) in enumerate(related)])
                # We need to keep the ordering intact
                res = list(brains)
                def _key(brain):
                    return positions.get(brain.UID, -1)
                res.sort(key=_key)
        return res

class SeminarsmainView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/seminarsmain.pt')

    def getSeminarsyear(self,yesno):
        yeardict = {}
        resultsfinal = []
        now = DateTime.DateTime()
        if (yesno == 1):
            results = self.context.portal_catalog.searchResults({"getSeminardate":{"query": now, "range": "min"}}, path={"query" : (self.context.portal_url.getPortalPath()+"/resources/seminars/")}, portal_type="Seminar", sort_on="getSeminardate", sort_order="ascending")
        else:
            results = self.context.portal_catalog.searchResults({"getSeminardate":{"query": now, "range": "max"}}, path={"query" : (self.context.portal_url.getPortalPath()+"/resources/seminars/")}, portal_type="Seminar", sort_on="getSeminardate", sort_order="descending")[:2]
        return results

    def getYear(self):
        return str(datetime.now())[:4]

class SeminarsyearView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/seminarsyear.pt')

    def getYear(self):
        return (self.request.get('URL')).rsplit('/',2)[1]

    def seminars(self):
        now = DateTime.DateTime()
        results = self.context.portal_catalog.searchResults({"getSeminardate":{"query": now, "range": "max"}}, path={"query" : ('/'.join(self.context.getPhysicalPath()))}, portal_type="Seminar", sort_on="getSeminardate", sort_order="descending")
        return results

class CsdView(BrowserView):
    """Default view of the CSD main page
    """
    __call__ = ViewPageTemplateFile('templates/csd.pt')

    def getSeminarsyear(self,yesno):
        yeardict = {}
        resultsfinal = []
        #import pdb; pdb.set_trace()
        #datenow = (datetime.now()).isocalendar()
        now = DateTime.DateTime()
        #self.context.getPlace()
        if (yesno == 1):
            results = self.context.portal_catalog.searchResults({"getSeminardate":{"query": now, "range": "min"}}, path={"query" : (context.portal_url.getPortalPath()+"/resources/seminars/")}, portal_type="Seminar", sort_on="getSeminardate", sort_order="ascending")
        else:
            results = self.context.portal_catalog.searchResults({"getSeminardate":{"query": now, "range": "max"}}, path={"query" : (context.portal_url.getPortalPath()+"/resources/seminars/")}, portal_type="Seminar", sort_on="getSeminardate", sort_order="descending")[:2]
        #Date={"query": datenow, "range": "min"},
        #getSeminardate="2011", 
        #p self.context.portal_catalog.searchResults ()
        return results

        #m = str(datenow[0])+'/'+str(datenow[1])+'/'+str(datenow[2])

    def getYear(self):
        return str(datetime.now())[:4]

class PressroomView(BrowserView):
    """Default view of the CSD main page
    """
    __call__ = ViewPageTemplateFile('templates/pressroom.pt')

    def getSeminarsyear(self,yesno):
        yeardict = {}
        resultsfinal = []
        #import pdb; pdb.set_trace()
        #datenow =  (datetime.now()).isocalendar()
        now = DateTime.DateTime()
        #self.context.getPlace()
        if (yesno == 1):
            results = self.context.portal_catalog.searchResults({"getSeminardate":{"query": now, "range": "min"}}, path={"query" : "/cipotato/resources/capacity-strengthening/seminars/"}, portal_type="Seminar", sort_on="getSeminardate", sort_order="ascending")
        else:
            results = self.context.portal_catalog.searchResults({"getSeminardate":{"query": now, "range": "max"}}, path={"query" : "/cipotato/resources/capacity-strengthening/seminars/"}, portal_type="Seminar", sort_on="getSeminardate", sort_order="descending")[:2]
        #Date={"query": datenow, "range": "min"},
        #getSeminardate="2011",
        #p self.context.portal_catalog.searchResults ()
        return results

        #m = str(datenow[0])+'/'+str(datenow[1])+'/'+str(datenow[2])

    def getYear(self):
        return str(datetime.now())[:4]

class LanguageSelector(BrowserView):
    implements(IViewlet)
    render = ViewPageTemplateFile('templates/languageselector.pt')

    def __init__(self, context, request, view, manager):
        super(LanguageSelector, self).__init__(context, request)
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def update(self):
        self.tool = getToolByName(self.context, 'portal_languages', None)

    def available(self):
        if self.tool is not None:
            selector = self.tool.showSelector()
            languages = len(self.tool.getSupportedLanguages()) > 1
            return selector and languages
        return False

    def portal_url(self):
        portal_tool = getToolByName(self.context, 'portal_url', None)
        if portal_tool is not None:
            return portal_tool.getPortalObject().absolute_url()
        return None

    def languages(self):
        """Returns list of languages."""
        if self.tool is None:
            return []

        bound = self.tool.getLanguageBindings()
        current = bound[0]

        def merge(lang, info):
            info["code"]=lang
            if lang == current:
                info['selected'] = True
            else:
                info['selected'] = False
            return info

        languages = [merge(lang, info) for (lang,info) in
                        self.tool.getAvailableLanguageInformation().items()
                        if info["selected"]]

        # sort supported languages by index in portal_languages tool
        supported_langs = self.tool.getSupportedLanguages()
        def index(info):
            try:
                return supported_langs.index(info["code"])
            except ValueError:
                return len(supported_langs)

        return sorted(languages, key=index)

    def showFlags(self):
        """Do we use flags?."""
        if self.tool is not None:
            return self.tool.showFlags()
        return False

class CalendarView(BrowserView):
    """View for CIP Calendar section
    """
    __call__ = ViewPageTemplateFile('templates/calendar.pt')

    def getThisMonth(self):
        #import pdb;pdb.set_trace()
        month = datetime.now().strftime("%m")
        monthen = month + "-ens"
        monthes = month + "-ens"
        results = []
        results.append(self.context.portal_catalog.searchResults(path={"query" : (self.context.portal_url.getPortalPath()+"/press-room/photo-gallery/general/cip-calendar")}, SearchableText=monthen)[0])
        results.append(self.context.portal_catalog.searchResults(path={"query" : (self.context.portal_url.getPortalPath()+"/press-room/photo-gallery/general/cip-calendar")}, SearchableText=monthes)[0])
        results.append(month)
        return results

    def getAllMonths(self):
        #import pdb;pdb.set_trace()
        eslist = []
        enlist = []
        results = []
        eslist = self.context.portal_catalog.searchResults(path={"query" : (self.context.portal_url.getPortalPath()+"/press-room/photo-gallery/general/cip-calendar")}, SearchableText="es.jpg", sort_order="ascending")
        enlist = self.context.portal_catalog.searchResults(path={"query" : (self.context.portal_url.getPortalPath()+"/press-room/photo-gallery/general/cip-calendar")}, SearchableText="standard.jpg", sort_order="descending")
        results.append(eslist)
        results.append(enlist)
        return results
