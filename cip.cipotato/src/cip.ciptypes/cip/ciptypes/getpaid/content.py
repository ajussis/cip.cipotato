from zope.interface import implements
from getpaid.core.interfaces import IBuyableContent

class BuyableContentAdapter(object):

    implements(IBuyableContent)

    def __init__(self, context):
        self.context = context
        price = context.getPrice()
        if (price):
            self.price = float(price)
        else:
            self.price = 0
        self.product_code = context.getPubcode()
