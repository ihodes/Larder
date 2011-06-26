import sys, getopt, core, parse, shopping

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
        return 1

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            return 1
        if o in ("-f", "--input-file"):
            larderfile = a
        else:
            larderfile=args[0]        
    if len(opts)==0: larderfile=args[0]

    parsed = parse.parse(larderfile)

def usage():
    print
    print "Usage:"
    print "\tfor now, run: \"python ledger.py ingredientfile.txt\""
    print
    print "Options:"
    print "\t -h, --help \t\t\t\t display this message"
    print "\t -f <file>, --input-file <file> \t parses the ingredients file provided"
    
if __name__ == "__main__":
    sys.exit(main())
