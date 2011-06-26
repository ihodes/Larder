"""
This modules contains methods to manipulate and query the items list.

item = {item:name quantity:quantity unit:unit_of_quantity price:price}
items = [item]
"""
# TODO: make QUANTITIES a sysem of equalities to make conversion easy & logical
QUANTITIES = ["lb", "lbs", "pound", "pounds", "oz", "ozs", "ounce", "ounces", \
                  "cup", "cups", "c", "teaspoon", "teaspoons", "tsp", "t",    \
                  "tablespoon", "tablespoons"] 


def printItem(item):
    """A nicer way to print out items"""
    print "%s: %i %s costs %.2f" % (item["item"], item["quantity"], item["unit"], item["price"])
