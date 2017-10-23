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


def to1005(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.policy.upgrades:to1005')
