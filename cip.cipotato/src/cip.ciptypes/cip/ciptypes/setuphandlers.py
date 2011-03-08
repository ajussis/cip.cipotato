from cStringIO import StringIO

from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.app.container.interfaces import INameChooser

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping, ILocalPortletAssignmentManager
from plone.portlet.collection.collection import Assignment
from plone.app.portlets.portlets import navigation

from Products.CMFPlone.utils import _createObjectByType
from Products.CMFCore.utils import getToolByName

def updateCatalog(context, clear=True):
    portal = context.getSite()
    logger = context.getLogger('cip.sppolicy updateCatalog')
    logger.info('Updating catalog (with clear=%s) so items in profiles/default/structure are indexed...' % clear )
    catalog = portal.portal_catalog
    err = catalog.refreshCatalog(clear=clear)
    if not err:
        logger.info('...done.')
    else:
        logger.warn('Could not update catalog.')

#def deletePloneFolders(p):
#    """Delete the standard Plone stuff that we don't need
#    """
#    # Delete standard Plone stuff..
#    existing = p.objectIds()
#    itemsToDelete = ['Members', 'news', 'events']
#    for item in itemsToDelete:
#        if item in existing:
#            p.manage_delObjects(item)

"""def createCompany(request, site, username, title, email, passwd=None):

    prepareMemberProperties(site)

    # portal_registrations manages new user creation
    regtool = getToolByName(site, 'portal_registration')

    # Default password to the username
    # ... don't do this on the production server!
    if passwd == None:
        passwd = username

    # Only lowercase allowed
    username = username.lower()

    # Username must be ASCII string
    # or Plone will choke when the user tries to log in
    username = str(username)

    def is_ascii(s):
        for c in s:
            if not ord(c) < 128:
                return False

        return True

    if not is_ascii(username):
        """ """
        IStatusMessage(request).addStatusMessage(_(u"Username must contain only characters a-z"), "error")
        return None

    # This is minimum required information set
    # to create a working member
    properties = {

        'username' : username,

        # Full name must be always as utf-8 encoded
        'fullname' : title.encode("utf-8"),
        'email' : email,
    }

    try:
        # addMember() returns MemberData object
        member = regtool.addMember(username, passwd, properties=properties)
    except ValueError, e:
        # Give user visual feedback what went wrong
        IStatusMessage(request).addStatusMessage(_(u"Could not create the user:") + unicode(e), "error")
        return None"""

def createGroups(portal):
    gr = portal.portal_groups
    group_ids = ['admins','human-resources','riu']
    for testGroup in group_ids:
        if not testGroup in gr.getGroupIds():
            gr.addGroup(testGroup)

def importPAS(portal):
    users_here = ['jussi;jussi;Jussi;Savolainen;ajussis@gmail.com','john;john1;John;Smith;john@mail.com','jens;jens;Jens;Riis;jens@mail.com','charles;charles;Charles;Day;charles@mail.com','michael;michael;Michael;Johnson;michael@mail.com','barbara;barbara;Barbara;Macintosh;barbara@mail.com','adelayde;adelayde;Adelayde;Rivas;adelayde@mailcom','vanessa;vanessa;Vanessa;Lopez;vanessa@mail.com']
#    users = users_here.data.split('\n')
    users = users_here
# add members to group
#    portal_groups = portal.portal_groups
# Add user to group "companies"
#portal_groups = site.portal_groups
#portal_groups.addPrincipalToGroup(member.getUserName(), "companies")
    regtool = getToolByName(portal, 'portal_registration')
    index = 1
    imported_count = 0
    for user in users:
        tokens = user.split(';')
        if len(tokens) == 5:
            passwd, id, last, first, email = tokens
            properties = {
                'username' : id,
                'fullname' : '%s %s' % (first, last),
                'email' : email,
            }
            try:
                regtool.addMember(id, passwd, properties=properties)
                print "Successfully added %s %s (%s) with email %s" % (first, last, id, email)
                imported_count += 1
            except ValueError, e:
                print "Couldn't add %s: %s" % (id, e)
        else:
            print "Could not parse line %d because it had the following contents: '%s'" % (index, user)
        index += 1
    print "Imported %d users (from %d lines of CSV)" % (imported_count, index)

def TEMPcreateFolderStructure(portal):
    """Define which objects we want to create in the site.
    """

    resources_children = [
        {   'id': 'publications',
            'title': 'Publications',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]
    potato_children = [
        {   'id': 'about-potato',
            'title': 'About Potato',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]
    sweetpotato_children = [
        {   'id': 'about-sweetpotato',
            'title': 'About Sweetpotato',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]
    andeanroots_children = [
        {   'id': 'about-andeanroots',
            'title': 'Andean Roots and Tubers',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]
    pressroom_children = [
        {   'id': 'news',
            'title': 'News',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]
    research_children = [
        {   'id': 'research-areas',
            'title': 'Research Areas',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]
    impacts_children = [
        {   'id': 'impact-story',
            'title': 'Impact Story',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]
    top_folders = [
        {   'id': 'resources',
            'title': 'Resources',
            'description': '',
            'type': 'Folder',
            'layout' : 'folder_listing',
            'children': resources_children,
            },
        {   'id': 'potato',
            'title': 'Potato',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': potato_children,
            },
        {   'id': 'sweetpotato',
            'title': 'Sweetpotato',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': sweetpotato_children,
            },
        {   'id': 'andeanroots',
            'title': 'Andean Roots and Tubers',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': andeanroots_children,
            },
        {   'id': 'press-room',
            'title': 'Press Room',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': pressroom_children,
            },
        {   'id': 'research',
            'title': 'Research',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': research_children,
            },
        {   'id': 'impacts',
            'title': 'Impacts',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': impacts_children,
            },
        ]

    createObjects(parent=portal, children=top_folders)

def createObjects(parent, children):
    """This will create new objects, or modify existing ones if id's and type
    match. In total 191.
    """
    parent.plone_log("Creating %s in %s" % (children, parent))
    existing = parent.objectIds()
    parent.plone_log("Existing ids: %s" % existing)
    for new_object in children:
        if new_object['id'] in existing:
            parent.plone_log("%s exists, skipping" % new_object['id'])
        else:
            _createObjectByType(new_object['type'], parent, \
                id=new_object['id'], title=new_object['title'], \
                description=new_object['description'])
        parent.plone_log("Now to modify the new_object...")
        obj = parent.get(new_object['id'], None)
        if obj is None:
            parent.plone_log("can't get new_object %s to modify it!" % new_object['id'])
        else:
            if obj.Type() != new_object['type']:
                parent.plone_log("types don't match!")
            else:
                obj.setLayout(new_object['layout'])
                obj.reindexObject()
                children = new_object.get('children',[])
                if len(children) > 0:
                    createObjects(obj, children)

def setupPortlets(site, out):
    # Register some portlets for this club's context.
    # Copied mostly from plone.portlets' README doctests.
    right = getUtility(IPortletManager, name='plone.rightcolumn')
    left = getUtility(IPortletManager, name='plone.leftcolumn')
    rightColumnInThisContext = getMultiAdapter((site, right), IPortletAssignmentMapping)
    leftColumnInThisContext = getMultiAdapter((site, left), IPortletAssignmentMapping)


    urltool  = getToolByName(site, 'portal_url')

#    projectCollectionPortlet = Assignment(header=u"Latest Projects 2",
#                                          limit=2,
#                                          target_collection = '/'.join(urltool.getRelativeContentPath(site.gpProjects)),
#                                          random=False,
#                                          show_more=True,
#                                          show_dates=False)

#    webmasterPortlet = Assignment(header=u"Control Panel",)

    def saveAssignment(mapping, assignment):
        chooser = INameChooser(mapping)
        mapping[chooser.chooseName(None, assignment)] = assignment

    saveAssignment(leftColumnInThisContext, projectCollectionPortlet)
#    saveAssignment(leftColumnInThisContext, webmasterPortlet)

def setSecuritySettings(portal):
    from plone.app.controlpanel.security import SecurityControlPanelAdapter
    settings = SecurityControlPanelAdapter(portal)
    settings.set_enable_self_reg(False)
    settings.set_allow_anon_views_about(False)
    settings.set_enable_user_folders(False)
    settings.set_enable_user_pwd_choice(True)


def setupAddableTypes(portal):
    # make root folder
    existing = portal.keys()
    if 'rootfolder' not in existing:
        portal.invokeFactory('Folder', id='cip', title='Home')
        portal.rootfolder.setConstrainTypesMode(1) # restrict what this folder can contain
        portal.rootfolder.setImmediatelyAddableTypes(['Folder'])
    #    portal.setLocallyAllowedTypes(['Folder'])
        portal.rootfolder.setLayout('frontpage')
        portal.rootfolder.reindexObject()

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    portal = context.getSite()

    if context.readDataFile('cip.cipotato_various.txt') is None:
        return
