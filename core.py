"""
This modules contains methods to manipulate and query the items list.

item = {item:name quantity:quantity unit:unit_of_quantity price:price}
items = [item]
"""
from fractions import Fraction

# TODO need to get rid of this, replace it with the generated graph
# this is used in tokenizeLineItem to capture units
# soln: add a nodes list to the graph, require a conversions file to be parsed 
#       before the items are? cons: slow? need a config file to specify
#       convrsions.txt file, or default to conversions.txt
QUANTITIES = ["lb", "lbs", "pound", "pounds", "oz", "ozs", "ounce", "ounces", \
                  "cup", "cups", "c", "teaspoon", "teaspoons", "tsp", "t",    \
                  "tablespoon", "tablespoons"] 

def convertUnit(amount, in_unit, out_unit):
    """Returns the number of out_units in amount of in_units."""
    pass

def printItem(item):
    """A nicer way to print out items"""
    print "%s: %i %s costs %.2f" % (item["item"], item["quantity"], item["unit"], item["price"])
