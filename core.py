"""
This modules contains methods to manipulate and query the items list.

    item = {item:name quantity:quantity unit:unit_of_quantity price:price}
    items = [item]
"""
from UserDict import IterableUserDict 
from UserList import UserList

class Item(IterableUserDict):
    """Represents a food ingredient with an item name, a price, and 
    possibly a quantity and unit amount (for the quantity: i.e. lbs, ounce)"""
    data = {}

    def __init__(self, item, price, unit="unit", quantity=1):
        self.data = {"quantity":quantity, "unit":unit, "item":item, "price":price}
        IterableUserDict.__init__(self, self.data)
        
class ItemList(UserList):
    """A list of items."""
    def __init__(self, data=None):
        UserList.__init__(self, data)

    def getItem(self, name=None, priceRange=None, unit=None):
        """Returns a list of items that match the params."""
        pass

class ShoppingList(ItemList):
    """A list of items to purchase"""
    def __init__(self, data=None):
        ItemList.__init__(self, data)
        


