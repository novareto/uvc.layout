from setuptools import setup, find_packages
import os

version = '1.3.3dev'

setup(name='uvc.layout',
      version=version,
      description="Basic Layout for UVC-Projects",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Christian Klinger',
      author_email='cklinger@novareto.de',
      url='http://www.novareto.de',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uvc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.testsetup',
          'grok',
          'dolmen.menu >= 0.2',
          'megrok.pagetemplate',
          'megrok.layout >= 1.0.1',
          'dolmen.app.layout >= 0.5',
          'dolmen.app.breadcrumbs >= 0.2',
          'zope.app.testing',
          'zope.testbrowser',
          'uvc.skin',
          'z3c.macro',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
