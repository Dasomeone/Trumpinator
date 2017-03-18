## Library Imports
import os
import argparse


## Setup Argparse for niceness
parser = argparse.ArgumentParser(description='Process Text-To-Speech commands')
parser.add_argument('textstring')

## Parse the arguments
args = parser.parse_args()

# DEBUG # Printing the text string to show we received input correctly.
print args.textstring

