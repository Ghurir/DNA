#!/usr/bin/python3

import sys, getopt, os

def main(argv):  
    def slice_str(text, step):
        return [text[i:i+step] for i in range(0, len(text), step)]
    
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print('unknown, use instead:')
        print('test.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    print('Input file is "', inputfile)
    
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    p = os.path.join(__location__, inputfile)
    
    original_code = ''
    with open(p,mode='r') as f:
        original_code = f.read()
    
    coddons = slice_str(original_code, 3)
    print(coddons)

if __name__ == "__main__":
   main(sys.argv[1:])
