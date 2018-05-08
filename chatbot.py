import sys

def waitForInput():
    message = input("")
    processMessage(message)

def processMessage(message):
    if(message == "bye"):
        print("Bye :(")
        sys.exit(1)
    print(">",message)
    waitForInput()


def main():
    waitForInput()

main()