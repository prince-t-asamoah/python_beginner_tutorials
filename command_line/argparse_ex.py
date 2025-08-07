import argparse

description_message = 'Adding description'
parser = argparse.ArgumentParser(description=description_message)
parser.add_argument('-o', '--Output', help='Show Output')
args = parser.parse_args()

if args.Output:
    print('Displaying Output as: % s' % args.Output)