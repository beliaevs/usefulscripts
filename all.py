import subprocess
import sys
from pathlib import Path


def main():
    forward_args = sys.argv[1:]
    p = Path('.')
    for d in p.glob('[a-zA-Z]*'):
        if d.is_dir():
            print(d)
            subprocess.run(forward_args, cwd = d)


if __name__=='__main__':
    main()



