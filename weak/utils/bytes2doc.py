import os
import sys

ENCODING='utf-8'
here = os.path.abspath(os.path.dirname(__file__))
DATADIR=os.path.join(here, '..', 'data')

def check_abs(s):
    if not os.path.isabs(s):
        s = os.path.join(DATADIR, s)
    return s

def base_to_c(s, base):
    try:
        assert base in [2, 16]
    except AssertionError:
        print("Only bases 16 and 2 supported now.")
    if base == 16:
        try:
            assert len(s) == 2
        except:
            print("Please try to convert a full byte (2 hex chars).")
    elif base == 2:
        try:
            assert len(s) == 8
        except:
            print("Please try to convert a full byte (8 bin chars).")
    return chr(int(s, base))
    
def main(infile, outfile, base):
    infile, outfile = check_abs(infile), check_abs(outfile)
    try:
        assert os.path.isfile(infile)
    except AssertionError:
        print("Can't find input file in this directory or the data directory.")
        return
    base = int(base)
    with open(infile, 'r') as f_in:
        with open(outfile, 'w') as f_out:
            while True:
                if base == 16:
                    s = f_in.read(2)
                elif base == 2:
                    s = f_in.read(8)
                else:
                    print("Only bases 16 and 2 supported now.")
                    return
                if not s:
                    break
                f_out.write(base_to_c(s, base))
            

if __name__ == "__main__":
    main(*sys.argv[1:])
