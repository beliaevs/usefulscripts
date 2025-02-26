import subprocess
import sys
from pathlib import Path


def main():
    forward_args = sys.argv[1:]
    if not forward_args:
        print('empty command')
        return

    p = Path('.')
    for d in p.glob('[a-zA-Z]*'):
        if d.is_dir():
            print(d)
            try:
                subprocess.run(forward_args, cwd = d, check=True, capture_output=True)
            except Exception as e:
                print(f'Error: {e}')


if __name__=='__main__':
    main()



