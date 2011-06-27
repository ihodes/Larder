"""
This modules contains methods to manipulate and query the items list.

item = {item:name quantity:quantity unit:unit_of_quantity price:price}
items = [item]
"""
from fractions import Fraction

def traverseWeightedTo(graph, init_weight, in_node, out_node):
    """Returns the the amount multiplied by the weights between in_node
    and out_node.

    A breadth-first traversal of the weighted graph from in_node to
    out_node, multiplying init_weight by the edge weight along the way"""
    edges = graph[1]
    visited_edges = set()
    next_nodes = [] # tuples of new starting nodes, plus new amount
    for node in edges:
        if node[0] == in_node:
            new_weight = node[2] * init_weight
            if node[1] == out_node: # total conversion done
                return new_weight
            else: # not done, but don't want to traverse again: 
                visited_edges.add(node)
                visited_edges.add((node[1], node[0], 1/node[2])) 
                next_nodes.append((new_weight, node[1]))
    for n in visited_edges: # don't use used edges
        edges.discard(n)
    for n in next_nodes:
        final = traverseWeightedTo((graph[0], edges), n[0], n[1], out_node)
        if final: return final
    return False # no luck

def convertTo(graph, amount, in_units, out_units):
    """Returns the number of out_units in amount of in_units."""
    return traverseWeightedTo(graph, amount, in_units, out_units)

def printItem(item):
    """A nicer way to print out items"""
    if len(item["unit"])>0: 
        print "%s: %i %s costs %.2f" % (item["item"], item["quantity"], \
                                            item["unit"], item["price"])
    else: 
        print "%s: %i costs %.2f" % (item["item"], item["quantity"], \
                                            item["price"])
