"""
This module handles the shopping cart.

A cart is a list of items:
cart = [item]
"""
import core 

def get_item(items, item_name):
    """Returns the item in items if it has name=item_name"""
    for item in items:
        if item_name == item["item"]:
            return item
    return None


# TODO: take unit type into account 
def calculateCart(cart, items, cgraph=None):
    """Takes items and amounts, compares it against the supplied items (from parse.parse)
    and returns the total price of the cart.
    
    If conversions are supplied, uses them to process cart."""
    price = 0
    warnings = "" # in case something isn't in item_list
    for item in cart:
        iname = item["item"]
        iquant = item["quantity"]
        iunit = item["unit"]
        listi = get_item(items, iname)
        if listi == None:
            warnings += "\n\t%s is not in the item list." % iname
        else:
            if cgraph and iunit != listi["unit"]: 
                print "converting", iname, "from", iunit, "to", listi["unit"]
                iquant = core.convertTo(cgraph, iquant, iunit, listi["unit"])
            if not iquant: raise Exception ("can't convert %s from %s" % (iname,iunit))
            price += (iquant * listi["price"])
    return (price, warnings)

