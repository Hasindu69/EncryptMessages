def shift_left_five_position(text):
    shifted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr(((ord(char) - ord('A') - 5) % 26) + ord('A'))
            elif char.islower():
                shifted_char = chr(((ord(char) - ord('a') - 5) % 26) + ord('a'))
        elif char.isdigit():
            shifted_char = str((int(char) - 5) % 10)  # Shift digits one position to the left
        else:
            shifted_char = char
        
        shifted_text += shifted_char
    
    return shifted_text

def getOriginal(text):
    shifted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + 5) % 26) + ord('A'))
            elif char.islower():
                shifted_char = chr(((ord(char) - ord('a') + 5) % 26) + ord('a'))
        elif char.isdigit():
            shifted_char = str((int(char) + 5) % 10)  # Shift digits one position to the left
        else:
            shifted_char = char
        
        shifted_text += shifted_char
    
    return shifted_text



print("Encryption and Decryption messages ")
print("Enter 1 to Encrypt Messages")
print("Enter 2 to Decrypt Messages")
print("Enter 0 to Exit")

userInput = int(input("Enter your number: "))

while True:
    if(userInput==1):
        oriText = input("Enter your text to Encrypt: ")
        shiftText = shift_left_five_position(oriText)
        print("Here's your Encrypted message: ",shiftText)
        break

    elif(userInput==2):
        oriText = input("Enter your Encrypted message: ")
        shiftText = getOriginal(oriText)
        print("Here's your Decrypted message: ", shiftText)
        break

    elif(userInput==0):
        print("Thank you for using our encryption application")
        break

    else:
        print("Enter a number in the description")
        
    