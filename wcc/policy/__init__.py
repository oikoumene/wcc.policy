from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable

class HiddenProducts(object):
    """This hides the upgrade profiles from the quick installer tool."""
    implements(INonInstallable)

    def getNonInstallableProducts(self):
        return [
            'wcc.policy.upgrades'
        ]


