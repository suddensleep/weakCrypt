import os
import sys

ENCODING='utf-8'
here = os.path.abspath(os.path.dirname(__file__))
DATADIR=os.path.join(here, '..', 'data')

def check_abs(s):
    if not os.path.isabs(s):
        s = os.path.join(DATADIR, s)
    return s

def c_to_base(c, base):
    hex_str = bytes(c, ENCODING).hex()
    if base == 16:
        return hex_str
    elif base == 2:
        return bin(int(hex_str, 16))[2:].zfill(8)
    else:
        return ""
    
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
                c = f_in.read(1)
                if not c:
                    break
                f_out.write(c_to_base(c, base))
            

if __name__ == "__main__":
    main(*sys.argv[1:])
