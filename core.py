"""
This modules contains methods to manipulate and query the items list.

    item = {item:name quantity:quantity unit:unit_of_quantity price:price}
    items = [item]
"""
from UserDict import IterableUserDict 
from UserList import UserList

class item(IterableUserDict):
    def __init__(self, name, price, unit="unit", quantity=1):
        IterableUserDict.__init__()

class ItemList(UserList):
    """Class """
    def __init__(self):
        UserList.__init__(self)

    def __init__(self, data):
        UserList.__init__(self, data)

    def getItem(self, name=None, priceRange=None, unit=None):
        """Returns a list of items that match the params."""
        
