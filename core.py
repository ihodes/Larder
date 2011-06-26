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

def traverseWeightedTo(graph, init_weight, in_node, out_node):
    """Returns the the amount multiplied by the weights between in_node
    and out_node.

    A breadth-first traversal of the weighted graph from in_node to
    out_node, multiplying init_weight by the edge weight along the way"""
    cgraph = graph
    next_nodes = [] # tuples of new starting nodes, plus new amount
    for node in cgraph:
        if node[0] == in_node:
            new_weight = node[2] * init_weight
            if node[1] == out_node: # total conversion done
                return new_weight
            else: # not done, but don't want to traverse again: 
                cgraph.remove(node) # remove edge from node
                cgraph.remove((node[1], node[0], 1/node[2])) # remove edge to
                next_nodes.append((new_weight, node[1]))
    for n in next_nodes:
        final = convertUnit(cgraph, n[0], n[1], out_node)
        if final: return final
    return False # no luck

def convertTo(graph, amount, in_node, out_node):
    return traverseWeightedTo(graph, amount, in_node, out_node)

def printItem(item):
    """A nicer way to print out items"""
    print "%s: %i %s costs %.2f" % (item["item"], item["quantity"], \
                                        item["unit"], item["price"])
