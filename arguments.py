import argparse


def main():
    parser = argparse.ArgumentParser(description = 'Testing commandline options')
    parser.add_argument('numbers', type=int, nargs='+')
    parser.add_argument('-in1', type = int, required = True, help = 'first argument')
    parser.add_argument('-in2', type = int, required = True, help = 'second argument')
    parser.add_argument('-op', choices=['sum', 'max'], required = True, help = 'operation choice')
    args = parser.parse_args()
    ops = {'sum': sum, 'max': max}
    print(f'sum: {args.in1 + args.in2}')
    print(f'{args.op} of separate numbers: {ops[args.op](args.numbers)}')


if __name__ == '__main__':
    main()