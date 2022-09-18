import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='what is the first number?')
    parser.add_argument('--y', type=float, default=1.0, help='what is the second number?')
    parser.add_argument('--operation', type=str, default='add', help=('Add, sub, mul, or div '))
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):

    if args.operation == 'Add':
        return args.x + args.y
    elif args.operation == 'Sub':
        return args.x - args.y
    elif args.operation == 'Mul':
        return args.x * args.y
    elif args.operation == 'Div':
        return args.x / args.y

if __name__ == '__main__':
    main()

