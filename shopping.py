# make QUANTITIES a sysem of equalities to make conversion easy & logical
QUANTITIES = ["lb", "lbs", "pound", "pounds", "oz", "ozs", "ounce", "ounces", \
                  "cup", "cups", "c", "teaspoon", "teaspoons", "tsp", "t",    \
                  "tablespoon", "tablespoons"] 

# A cart is a list of cartitems that may be purchased. The prices of items are defined by 
# items_list a result of parse.parse.
# 
# cartitem = {"item":itemname "quantity":quantity}
# cart = [cartitem] 

def calculateCart(cart, items_list):
    """Takes items and amounts, compares it against the supplied items_list (from parse.parse)
    and returns the price of the cart"""
    prices = []
    for item in cart:
        if item["item"]
