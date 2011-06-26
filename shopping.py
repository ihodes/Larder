"""
This module handles the shopping cart.
"""
# A cart is a list of cartitems that may be purchased. The prices of items are defined by 
# items_list a result of parse.parse.
# 
# cartitem = {"item":itemname "quantity":quantity}
# cart = [cartitem] 

def get_item(items, item_name):
    """Returns the item in items if it has name=item_name"""
    for item in items:
        if item_name == item["item"]:
            return item
    return None


# TODO: take unit type into account (need to do this all over)
def calculateCart(cart, items):
    """Takes items and amounts, compares it against the supplied items (from parse.parse)
    and returns the total price of the cart"""
    price = 0
    warnings = "" # in case something isn't in item_list
    for item in cart:
        print item
        iname = item["item"]
        print iname
        iquant = item["quantity"]
        listi = get_item(items, iname)
        if listi == None:
            warnings += "\n\t%s is not in the item list." % iname
        else:
            price += (iquant * listi["price"])
    return (price, warnings)

