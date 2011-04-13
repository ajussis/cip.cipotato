from Products.CMFPlone.utils import _createObjectByType

def updateCatalog(context, clear=True):
    portal = context.getSite()
    logger = context.getLogger('cip.cipotatotheme updateCatalog')
    logger.info('Updating catalog (with clear=%s) so items in profiles/default/structure are indexed...' % clear )
    catalog = portal.portal_catalog
    err = catalog.refreshCatalog(clear=clear)
    if not err:
        logger.info('...done.')
    else:
        logger.warn('Could not update catalog.')

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('cip.cipotatotheme_various.txt') is None:
        return

    # Add additional setup code here
    
    portal = context.getSite()

    existing = portal.keys()

    """if 'cipnews' not in existing:
        _createObjectByType('Topic', portal, id='cipnews', title='Latest News',
                            description='Show the latest news')
        theCollection = portal.cipnews
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(2)
        path_crit = theCollection.addCriterion('path','ATRelativePathCriterion')
        path_crit.setRelativePath('../')
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue(['News Item'])

    if 'cipinthenews' not in existing:
        _createObjectByType('Topic', portal, id='cipinthenews', title='Latest CIP in the News',
                            description='Show the latest CIP in the News')
        theCollection = portal.cipinthenews
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)
        path_crit = theCollection.addCriterion('path','ATRelativePathCriterion')
        path_crit.setRelativePath('../')
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue(['CIPintheNews'])

    if 'featured' not in existing:
        _createObjectByType('Topic', portal, id='featured', title='Latest Featured Publications',
                            description='Show the latest Featured Publications')
        theCollection = portal.featured
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)
        path_crit = theCollection.addCriterion('path','ATRelativePathCriterion')
        path_crit.setRelativePath('../')
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue(['Publication'])
    """
    #    updateCatalog()