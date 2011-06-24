import sys
import getopt
import re
from fractions import Fraction

ING_REGEX = r"([0-9]*/?[0-9]*)\s*(.*)"
# make QUANTITIES a sysem of equalities to make conversion easy & logical
QUANTITIES = ["lb", "lbs", "pound", "pounds", "oz", "ozs", "ounce", "ounces", \
                  "cup", "cups", "c", "teaspoon", "teaspoons", "tsp", "t", \
                  "tablespoon", "tablespoons"] 
FLAGS = "hf:"
OPTIONS = ["help", "input-file="]

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], FLAGS, OPTIONS)
    except Exception: 
        print "---Incorrect Usage---"
        usage()
        return 0

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            return 1
        if o in ("-f", "--input-file"):
            larderfile = a
        else:
            larderfile=args[0]        
    if len(opts)==0: larderfile=args[0]

    parse(larderfile)


def tokenizeLine(line):
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
    price = Fraction(line[1])
    item = m.group(2)
    unit = "unit"

    # see if the item is modified by a unit type
    ti = item.split(" ")[0]
    if ti in QUANTITIES: 
        item = "".join(item.split(" ")[1:])
        unit = ti

    return {"quantity":quant, "unit":unit, "item":item, "price":price}

def parse(larderfile, parseopts=None):
    items = []
    for line in open(larderfile):
        items.append(tokenizeLine(line))

    for i in items:
        print i

def usage():
    print
    print "Usage::"
    print "\tfor now, run: \"python ledger.py ingredientfile.txt\""
    print
    print "Options:"
    print "\t -h, --help \t\t\t\t display this message"
    print "\t -f <file>, --input-file <file> \t parses the ingredients file provided"
    
if __name__ == "__main__":
    sys.exit(main())
