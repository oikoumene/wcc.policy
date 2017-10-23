from collective.grok import gs
from Products.CMFCore.utils import getToolByName
from wcc.featurable.interfaces import IFeaturable
from zope.component import getUtility
from zope.component.hooks import getSite
from plone.app.layout.navigation.root import getNavigationRoot
from logging import getLogger
from Products.Archetypes import atapi
from archetypes.schemaextender.field import ExtensionField
import sys
from plone.app.blob.field import ImageField as BlobImageField
logger = getLogger('wcc.policy.upgrade')



@gs.upgradestep(title=u'Upgrade wcc.policy to 1005',
                description=u'disables translation on edit bar',
                source='1004', destination='1005',
                sortkey=1, profile='wcc.policy:default')
def 1005(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.policy.upgrades:1005')
