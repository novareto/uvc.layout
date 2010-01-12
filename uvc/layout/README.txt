Functional Doctest
==================

:Test-Layer: functional

Setup
-----

Befor we can start to test the StandardLayout and the ViewletManagers
we have to setup a "kind of a" to access the layout with a TestRequest.

Here we create the Simple Site:

   >>> import grok
   >>> from persistent import Persistent
 
   >>> from zope.app.container import btree
   >>> class Uvcsite(btree.BTreeContainer):
   ...     """Sample container."""
   ...     __name__ = u'container'

Here we create a simple View for this Site:

   >>> from megrok.layout import Page
   >>> class Index(Page):
   ...    grok.context(Uvcsite)
   ...    def render(self):
   ...        return "klaus"

   >>> from grokcore.component.testing import grok_component

   >>> grok_component('Index', Index)
   True

We persist the Site:

   >>> root = getRootFolder()
   >>> uvcsite = Uvcsite()
   >>> root['app'] = uvcsite



The Layout
----------

Now we are able to access the Index View via the Site and a TestRequest

   >>> from zope.publisher.browser import TestRequest
   >>> from zope.component import getMultiAdapter

   >>> view = getMultiAdapter((uvcsite, TestRequest()), name="index")
   >>> view
   <Index object at ...>

   >>> print view()
   <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
             "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
   <html xmlns="http://www.w3.org/1999/xhtml">
   <head>
     <title>Extranet</title>
   </head>
   <body>
     <div id="page">
       <div id="header">
       </div>
       <div class="content">
         <div class="left-col">
           <div class="box">
           </div>
           <div class="box">
           </div>
         </div>
         <div class="right-col">
            <div clss="breadcrum">
       <p> Sie sind hier:
          <a href=http://127.0.0.1/app> app </a>/
       </p>
   </div>
   <div class="relax"> </div>
            <div>
   </div>
            <div>klaus</div>
         </div>
         <div class="relax"> </div>
       </div>
       <div class="footer">
   <div class="relax"> </div>
   </div>
     </div>
   </body>
   </html>

