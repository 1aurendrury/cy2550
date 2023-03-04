#!/usr/bin/env python3
import random
import argparse
wordfile = open("words.txt")

parser = argparse.ArgumentParser()
parser.add_argument("-w", type=int, default=4)
parser.add_argument("-c", type=int, default=0)
parser.add_argument("-s", type=int, default=0)
parser.add_argument("-n", type=int, default=0)
args = parser.parse_args()

randomPassword = random.sample(wordfile.read().splitlines(), args.w)

## initial lists of input & amount of recursions
initialCapsArray = []
initialNumOfCaps = 0
initialSymbolsArray = []
initialNumOfSymbols = 0
initialNumberArray = []
initialNumOfNumbers = 0
listOfSymbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ":", ";", 
        "?", "/", "<", ">"]

## capital letters
if (args.c > 0 and args.c <= args.w):
    capsWords = random.sample(randomPassword, args.c)
    intermediateSet = set(capsWords)
    randomPassword = [x for x in randomPassword if x not in intermediateSet]
    while (initialNumOfCaps < args.c):
        initialCapsArray.append(capsWords[initialNumOfCaps].title())
        initialNumOfCaps = initialNumOfCaps + 1
randomPassword = randomPassword + initialCapsArray


## symbols
if (args.s > 0):
    while (initialNumOfSymbols < args.s):
        intermediateSymb = random.sample(listOfSymbols, 1)
        initialSymbolsArray = initialSymbolsArray + intermediateSymb
        initialNumOfSymbols = initialNumOfSymbols + 1
randomPassword =  initialSymbolsArray + randomPassword


## numbers
if (args.n > 0):
    while (initialNumOfNumbers < args.n):
        listofRandNums = [str(random.randint(0,9))]
        initialNumberArray = initialNumberArray + listofRandNums
        initialNumOfNumbers = initialNumOfNumbers + 1
randomPassword = randomPassword + initialNumberArray

## print the password here
print("".join(randomPassword))
