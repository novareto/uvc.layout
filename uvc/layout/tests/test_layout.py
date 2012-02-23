import re
import unittest
import doctest
import uvc.layout
from pkg_resources import resource_listdir
from zope.testing import cleanup, renormalizing
import zope.component.eventtesting

from zope.app.wsgi.testlayer import BrowserLayer

FunctionalLayer = BrowserLayer(uvc.layout)


def setUpZope(test):
    zope.component.eventtesting.setUp(test)

def cleanUpZope(test):
    cleanup.cleanUp()


def suiteFromPackage(name):
    files = resource_listdir(__name__, name)
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename.endswith('_fixture.py'):
            continue
        if filename == '__init__.py':
            continue

        dottedname = 'uvc.layout.tests.%s.%s' % (name, filename[:-3])
        test = doctest.DocTestSuite(dottedname,
                                    #setUp=setUpZope,
                                    extraglobs=dict(getRootFolder=FunctionalLayer.getRootFolder,),
                                    #tearDown=cleanUpZope,
                                    optionflags=doctest.ELLIPSIS+
                                    doctest.NORMALIZE_WHITESPACE)
        test.layer = FunctionalLayer
        suite.addTest(test)
    return suite

def test_suite():
    suite = unittest.TestSuite()
    for name in ['uvclayout']:
        suite.addTest(suiteFromPackage(name))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
