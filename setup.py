from setuptools import setup, find_packages
import os

version = '1.26.3.dev0'

setup(name='wcc.policy',
      version=version,
      description="WCC site content customizations",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://github.com/inigoconsulting/wcc.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['wcc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.multilingual',
          'plone.multilingualbehavior',
          'redturtle.video',
          'collective.rtvideo.youtube',
          'collective.rtvideo.vimeo',
          'Products.ContentWellPortlets',
          'wcc.theme',
          'wcc.common',
          'wcc.churches',
          'eea.facetednavigation',
          'collective.socialbar',
          'Products.BlingPortlet',
          'collective.contentleadimage',
          'Products.RedirectionTool',
          'wcc.prayercycle',
          'wcc.featurable',
          'collective.carousel',
          'collective.portlet.collectionmultiview',
          'wcc.carousel',
          'wcc.weeklynews',
          'wcc.activity',
          'wcc.content',
          'wcc.rawhtml',
          'wcc.importer',
          'wcc.audiofile',
          'collective.quickupload',
          'wcc.document',
          'wcc.donation',
          'collective.documentviewer',
          'wcc.multilingual',
          'wcc.homepage',
          'wcc.watertheme',
          'wcc.socialportlet',
          'wcc.contactform',
          'wcc.caching',
          'wcc.remotenews',
          'wcc.jsonapi',
          'Products.feedfeeder',
          'wcc.search',
          'wcc.books',
          'wcc.externalscripts',
          'collective.recaptcha',
          'collective.captchacontactinfo',
          'wcc.committee',
          'collective.plonetruegallery',
          'collective.ptg.allnewest',
          'wccresponsive.theme',
          'wcc.footer',
          'Products.PloneKeywordManager',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone

      """,
      )
