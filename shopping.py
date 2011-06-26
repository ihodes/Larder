"""
This module handles the shopping cart.
"""
# A cart is a list of cartitems that may be purchased. The prices of items are defined by 
# items_list a result of parse.parse.
# 
# cartitem = {"item":itemname "quantity":quantity}
# cart = [cartitem] 

def get_item(item_list, item_name):
    """Returns the item in item_list if it has name=item_name"""
    for item in item_list:
        if item_name == item["item"]:
            return item
    return None

def calculateCart(cart, items_list):
    """Takes items and amounts, compares it against the supplied items_list (from parse.parse)
    and returns the total price of the cart"""
    price = 0
    warnings = "" # in case something isn't in item_list
    for item in cart:
        iname = item["name"]
        iquant = item["quantity"]
        listi = in_list(item_list, iname)
        if listi == None:
            warnings += "%s is not in the item list.\n" % iname
        else:
            price += (iquant * listi["price"])
    return (price, warnings)
        
