import sys, getopt, core, parse, shopping

FLAGS = "hf:spdc:"
OPTIONS = ["help", "input-file=", "shopping", "debug-on", "print-items", \
               "conversions="]

def main(argv=None):
    print "Larder: -h or --help for information\n"
    if argv is None:
        argv = sys.argv
    if not len(argv)>1:
        usage()
    try:
        opts, args = getopt.getopt(argv[1:], FLAGS, OPTIONS)
    except Exception: 
        usage()

    shop = False
    printing = False
    debug = False
    infile = None
    items = None
    conversions = None
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
            cart = parse.parse(sys.stdin)
            shop = True
        if o in ("-p", "--print-items"):
            printing = True
        if o in ("-d", "--debug-on"):
            debug = True
        if o in ("-c", "--conversions"):
            conversions = open(a)

    if infile: items = parse.parse(infile, "norm")

    if shop: 
        scalc = shopping.calculateCart(cart, items)
        print "\n\nTotal cost of cart is $%.2f" % scalc[0]
        if len(scalc[1])>1:
            print "warnings: %s" % scalc[1]
        print 

    if printing:
        for item in items:
            core.printItem(item)
        
    if debug:
        print "\nDEBUG ON\n"
        print "opts:", opts, " args: ", args
        print items

    if conversions:
        print "doing that"
        print parse.parseConversions(conversions)

    return 0

def usage():
    print
    print "Usage:"
    print "\tlarder.py [-shdp] [-f] larderfile"
    print
    print "Options:"
    print "\t -h, --help \t\t\t\t display this message"
    print "\t -f <file>, --input-file <file> \t parses the ingredients file provided"
    print "\t -p, --print-items \t\t\t pretty-prints the items from the ingredient file"
    print "\t -d, --debug-on \t\t\t runs larder in debug mode"
    print "\t -s, --shopping \t\t\t reads shopping cart from stdin and prints its price"
    return 0
    
if __name__ == "__main__":
    sys.exit(main())
