"""
This module is used to parse the various input files and store them in
the correct internal form.
"""
import re, core
from fractions import Fraction

ING_REGEX = r"([0-9]*/?[0-9]*)\s*(.*)"

def tokenizeLineItem(line, units=None):
    """Splits a larderfile line into proper tokens"""
    raw_line = line.strip().split("=")
    line = []
    tokens = []
    for t in raw_line: line.append(t.strip())

    ingredient = line[0]

    m = re.match(ING_REGEX, ingredient)
    if not m: return None

    if m.group(1): quant = Fraction(m.group(1))
    else: quant = Fraction(1)
    try: 
        price = Fraction(line[1])
    except: 
        price = Fraction()
    item = m.group(2)
    unit = ""

    # see if the item is modified by a unit type
    if units:
        ti = item.split(" ")[0]
        if ti in units: ## need to fix this: use the conversions file instead of hardcoding
            item = " ".join(item.split(" ")[1:])
            unit = ti

    return {"item":item, "price":price, "unit":unit, "quantity":quant}

def normalizeItem(item):
    """"Returns the item hash with quantity 1, and price normalized to 1 unit """
    item["price"] = item["price"]/item["quantity"]
    item["quantity"] = 1
    return item
 
def parse(infile, parseopts=None, units=None):
    """Returns a list of normalized items."""
    items = []
    for line in infile:
        if len(line)>1:
            item = tokenizeLineItem(line, units)
            if parseopts=="norm": item = normalizeItem(item)
            items.append(item)
    return items


def parseConversions(infile, parseopts=None):
    """Returns a weighted directed  graph to be used for conversions. 
    Generated from the infile.

    infile must have lines of the form: 
        n unit1 = m unit2
    where n and m are arbitrary rational numbers, or blank (=1).

    graph = [[node], [edge]]
    node = String
    edge = (node_origin, node_dest, C)
           where C is the conversion factor between node_origin and 
           node_dest"""
    edges = []
    nodes = set()
    reg = r"(\d*/?\.?\d+)?\s*(\w+)"
    for line in infile: 
        if len(line)>1:
            splits = line.split("=")
            f = re.match(reg, splits[0]).groups()
            g = re.match(reg, splits[1]).groups()
            n = m = Fraction(1)
            if f[0]: n = Fraction(f[0])
            if g[0]: m = Fraction(g[0])
            nodes.add(f[1])
            edges.append((f[1], g[1], m/n))
            edges.append((g[1], f[1], n/m))
    return (nodes, edges)
    
            
