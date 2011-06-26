"""
This module is used to parse the various input files and store them in 
the correct internal form.
"""
import re, core
from fractions import Fraction

ING_REGEX = r"([0-9]*/?[0-9]*)\s*(.*)"

def tokenizeLineItem(line):
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
    ti = item.split(" ")[0]
    if ti in core.QUANTITIES: 
        item = "".join(item.split(" ")[1:])
        unit = ti

    return {"item":item, "price":price, "unit":unit, "quantity":quant}

def normalizeItem(item):
    """"Returns the item hash with quantity 1, and price normalized to 1 unit """
    item["price"] = item["price"]/item["quantity"]
    item["quantity"] = 1
    return item
 
def parse(infile, parseopts=None):
    """Returns a list of normalized items."""
    items = []
    for line in infile:
        if len(line)>1: items.append(tokenizeLineItem(line))
    return items
