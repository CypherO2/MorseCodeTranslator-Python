MorseKey = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

testCode1 = "-.--.-"
testCode2 = "test."


# Initial Function Declaring User's Choice
def main():
    menuChoice = input(
        "What would you link to do?\n1. Encrypt Text\n2. Decrypt Code\n> > > "
    )
    while int(menuChoice) not in range(1, 3):
        menuChoice = input(
            "Please enter a valid response!\n1. Encrypt Text\n2. Decrypt Code\n> > > "
        )
    if menuChoice == "1":
        Encryption()
    elif menuChoice == "2":
        Decryption()
    else:
        raise Exception(
            "Something went wrong during the initial input sequence!\n Line 49 -> 65"
        )
    return


# Function that handles the encryption of text
def Encryption():
    # print("Encryption") - Test Complete
    userText = input("What would you like to encrypt?\n> > > ")
    while type(userText) == str and userText != "":
        userText = input("What would you like to encrypt?\n> > > ")
    return


# Function to handle validation of morse code
def MorseValidation(morseCode):
    for morse in morseCode:
        while morse == "." or morse == "-":
            return "Code Morsing"
        else:
            return "Not Very Morse"
    return


# Function that handles the decryption of morse code
def Decryption():
    # print("Decryption") - Test Complete
    userCode = testCode2  # input("What would you like to decrypt?\n> > > ")
    print(MorseValidation(userCode))  # Validation Function
    return


if __name__ == "__main__":
    main()
