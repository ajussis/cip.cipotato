from zope.interface import implements
from getpaid.core.interfaces import IBuyableContent

class BuyableContentAdapter(object):

    implements(IBuyableContent)

    def __init__(self, context):
        self.context = context
        self.price = float(context.getPrice())
        self.product_code = context.getPubcode()
