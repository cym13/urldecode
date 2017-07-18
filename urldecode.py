#!/usr/bin/env python3

"""Encode and decode using URL encoding

Usage: urldecode [-h] [-e] STRING...

Options:
    -h, --help      Print this help and exits
    -e, --encode    Encode the string instead of decoding it

Arguments:
    STRING  String to be decoded or - for stdin"""


import sys
import urllib.parse


def parse_args(raw_args):
    args = raw_args

    if len(args) == 0:
        print(__doc__)
        sys.exit(1)

    should_encode = False
    for arg in raw_args:
        if arg == "--":
            args.remove("--")
            break

        elif arg == "-e":
            should_encode = True
            args.remove("-e")

        elif arg == "-h" or arg == "--help":
            print(__doc__)
            sys.exit(0)

    return args, should_encode


def main():
    args, should_encode = parse_args(sys.argv[1:])

    transform = urllib.parse.quote if should_encode else urllib.parse.unquote

    for arg in args:
        if arg == '-':
            print(transform(sys.stdin.read()))

        else:
            print(transform(arg))


if __name__ == "__main__":
    main()
