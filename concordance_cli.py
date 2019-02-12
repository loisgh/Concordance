from concordance import *
import sys


def main(in_file_name):
    """ This is a script for running the concordance classes at the command line"""
    CreateConcordance.concordance(in_file_name)


file_name = sys.argv[1]
main(file_name)
