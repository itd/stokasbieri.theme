from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize

from plone.app.layout.viewlets import common

import DateTime

class SearchBoxViewlet(common.SearchBoxViewlet):
    """A customixed version of the searchbox
    """
    index = ViewPageTemplateFile('bieri_searchbox.pt')


class BieriPictureBoxViewlet(ViewletBase):
    """A viewlet that contains pictures and some info
    """
    index = ViewPageTemplateFile('bieri_picturebox.pt')


class BieriGlobalSectionsViewlet(common.GlobalSectionsViewlet):
    """override of the somewhat lacking GlobalSectionsViewlet
    """
    @memoize
    def bieriDate(self):
        now = DateTime.DateTime()
        foo = "%s, %s %d, %d" % (now.Day(), now.Month(), now.day(), now.year())
        #import pdb; pdb.set_trace()
        return foo

    index = ViewPageTemplateFile('bieri_globalnav.pt')
