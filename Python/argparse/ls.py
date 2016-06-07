#!/usr/bin/env python
'''
A Python script that implements the functionality of the GNU 'ls' command using argparse and os.
This will accomplish the following:
    a) Force me to read the man file for GNU ls more thoroughly.
    b) Allow me to get better at using argparse.
    c) Understand how to more effectively interact with the system using the os module.
'''
import argparse
import os

def default(path):
    '''
    This function implements the default functionality of ls (i.e., when called with no flags)
    and constitutes a minimum viable product.
    '''
    if not os.path.exists(path):
        print "ls.py: cannot access %s: No such file or directory" % path
        return
    items = sorted(os.listdir(path))
    #TODO Better output formatting.
    print "\t\t".join(items)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Processes the flags for the ls command.")
    parser.add_argument("path", nargs="?", type=str, metavar="PATH", default=os.getcwd(),
                        help="A path to the directory whose contents you would like to list.")
    args = parser.parse_args()
    default(args.path)
