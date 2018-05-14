import sys
import re

data = [
    {'match':["(.*)hoe lang( duurt)? de opleiding"], "message":"De opleiding duurt 4 jaar, maar soms loopt het iets uit."},
    {'match':["wat leer (ik|je)( zoal)? tijdens de opleiding"], "message":"Je leert programmeren en verschillende skills die van pas kunnen komen in het bedrijfsleven."},
    {'match':[], "message":""},
    {'match':[], "message":""}
]

def waitForInput():
    message = input("")
    processMessage(message)

def processMessage(message):
    if(re.match("^(doei|tot ziens)$", message)):
        print("Tot ziens!")
        sys.exit(1)
    print(">", getMatches(message))
    waitForInput()

def getMatches(message):
    for option in data:
        for match in option['match']:
            if(re.match(match, message, re.IGNORECASE)):
                return option['message']
    return "Sorry, ik begreep je niet. Zou je het op een andere manier kunnen vragen?"


def main():
    print("Wat zou je willen weten?")
    waitForInput()

main()