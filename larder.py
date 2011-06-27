import sys, getopt, core, parse, shopping

FLAGS = "hf:spd"
OPTIONS = ["help", "input-file=", "shopping", "debug-on", "print-items", \
               "conversions=", "precise"]
CONVERSIONS_FILE = "conversions.txt"

def main(argv=None):
    print "Larder: -h or --help for information\n"
    if argv is None:
        argv = sys.argv
    if not len(argv)>1:
        usage()
        return 1
    try:
        opts, args = getopt.getopt(argv[1:], FLAGS, OPTIONS)
    except Exception: 
        print "Error: options are malformed."
        usage()
        return 1
    
    shop = False
    printing = False
    debug = False
    precise = False
    infile = None
    items = None
    try: conversions = open(CONVERSIONS_FILE)
    except Exception: pass
    if len(args)>0: infile=open(args[0]) 

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            return 1
        if o in ("-f", "--input-file"):
            infile = open(a)
        if o in ("-s", "--shopping"):
            print "Enter your shopping list below [^D when done]"
            print "(lines should be in the form:  [quantity] [unit] <item>) \n"
            shop = True
        if o in ("-p", "--print-items"):
            printing = True
        if o in ("-d", "--debug-on"):
            debug = True
        if o in ("--conversions"):
            conversions = open(a)
        if o == "--precise":
            precise = True

    cgraph = parse.parseConversions(conversions)
    if infile: items = parse.parse(infile, parseopts="norm", units=cgraph[0])
    if shop: cart = parse.parse(sys.stdin, units=cgraph[0])

    if shop: 
        scalc = shopping.calculateCart(cart, items, cgraph)
        if not precise: print "\n\nTotal cost of cart is $%.2f" % scalc[0]
        else: print "\n\nTotal cost of cart is $s" % str(scalc[0])
        if len(scalc[1])>1:
            print "warnings: %s" % scalc[1]
        print 

    if printing:
        for item in items:
            core.printItem(item, precise)


    if debug:
        print "\nDEBUG ON"
        print "opts:", opts, " args: ", args
        print "Items:\n", items
        print "\nPrinting conversion graph:"
        for node in cgraph[0]:
            print node
        for edge in cgraph[1]:
            print edge
    return 0

def usage():
    print
    print "Usage:"
    print "\tlarder [-shcdp] [-f] larderfile"
    print
    print "Options:"
    print "\t -h, --help \t\t\t\t display this message"
    print "\t -f <file>, --input-file <file> \t parses the ingredients file provided"
    print "\t -p, --print-items \t\t\t pretty-prints the items from the ingredient file"
    print "\t -d, --debug-on \t\t\t runs larder in debug mode"
    print "\t -s, --shopping \t\t\t reads shopping cart from stdin and prints its price"
    print "\t --conversions <conversionfile>  \t uses <conversionfile> for conversions"
    print "\t --precise  \t\t\t\t prints prices in rationals"
    
if __name__ == "__main__":
    sys.exit(main())
