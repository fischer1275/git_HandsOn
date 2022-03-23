#!/usr/bin/env python

import sys, re		#Imports necessary dependencies/libraries
from argparse import ArgumentParser	#imports specific function from library 

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')	                #creates a parser object with description 
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")        #generates sequence input variable
parser.add_argument("-m", "--motif", type = str, required = False, help = "anything")           #generates motif input variable 


if len(sys.argv) == 1:          #checks how many arguments were given/ if just 1 is given, code stops and help is displayed
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()                          #set args variable to values of parsed arguments (-s & -m)

args.seq = args.seq.upper()                                     # convert all input into upper case
if re.search('^[ACGTU]+$', args.seq):                           # check if any ACGTU is in the sequence
    if re.search('T', args.seq) and re.search('U', args.seq):   # check if both T & U are present in the sequence
        print("Error: sequence contains T & U")
    elif re.search('T', args.seq):                      # check if any T is in the sequence & U is not 
        print ('The sequence is DNA')
    elif re.search('U', args.seq):                      # check if any U is in the sequence & T is not 
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')    #if neiter T or U is present in the sequence to identify DNA or RNA 
else:
    print ('The sequence is not DNA nor RNA')       


if args.motif:                                      #Check if a motif was given 
    args.motif = args.motif.upper()                 #convert motif to uppercase 
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):             #if motif is found in sequence print
        print("A MOTIF WAS FOUND")
    else:
        print("NOTHING HAS BEEN FOUND")
