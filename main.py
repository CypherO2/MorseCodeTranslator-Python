morseKey = {}

with open("morsecodeKey.txt","r") as morseKey_RAW:
    morseKey_RAW = morseKey_RAW.read()
    morseKey_RAW = morseKey_RAW.split("~")
    for KeyVal in morseKey_RAW:
        pair = KeyVal.split(":")
        key, val = pair[0], pair[1]
        morseKey[key] = val

# print(morseKey)

testCode1 = "-.--.-"
testCode2 = "test."


# Initial Function Declaring User's Choice
def main() -> None:
    menuChoice = input(
        "What would you like to do?\n1. Encrypt Text\n2. Decrypt Code\n> > > "
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
            "Something went wrong during the initial input sequence!\n Line 25 -> 41"
        )


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

    if morseCode in morseKey.values():
        return "Morse Code is Very Morse"
    elif morseCode not in morseKey.values():
        return "Morse Not Code"   
    

    return


# Function that handles the decryption of morse code
def Decryption():
    # # print("Decryption") - Test Complete
    # userCode = testCode2  # input("What would you like to decrypt?\n> > > ")
    # print(MorseValidation(userCode))  # Validation Function
    print("Not Yet Implemented")
    main()
    return


if __name__ == "__main__":
    main()
