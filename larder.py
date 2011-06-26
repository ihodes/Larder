import sys, getopt, core, parse, shopping

FLAGS = "hf:s"
OPTIONS = ["help", "input-file=", "shopping"]

def main(argv=None):
    print "Larder: -h or --help for information"
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], FLAGS, OPTIONS)
    except Exception: 
        print "---Incorrect Usage---"
        usage()
        return 1
    print "opts:", opts, " args: ", args

    if len(args)>0: infile=open(args[0])

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            return 1
        if o in ("-f", "--input-file"):
            infile = open(a)
        if o in ("-s", "--shopping"):
            cart = parse.parse(sys.stdin)

    items = parse.parse(infile)

    print
    for i in items:
         core.printItem(i)


def usage():
    print
    print "Usage:"
    print "\tlarder.py [-sh] [-f] larderfile"
    print "\tfor now, run: \"python ledger.py ingredientfile.txt\""
    print
    print "Options:"
    print "\t -h, --help \t\t\t\t display this message"
    print "\t -f <file>, --input-file <file> \t parses the ingredients file provided"
    
if __name__ == "__main__":
    sys.exit(main())
