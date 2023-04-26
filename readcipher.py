import sys
import re
file = open('inputtext.txt', 'r')
def decrypt_caesar(message, shift):
    #print(message)
    #print(shift)
    decrypted_message = ""
    new_message = None
    new_message = re.sub(r'[^\w\s]', '', message)
    for char in new_message.upper():
        if char.isalpha():
            shift_value = shift
            if char.islower():
                decrypted_message += chr((ord(char) - 97 + shift_value) % 26 + 97)
            else:
                decrypted_message += chr((ord(char) - 65 + shift_value) % 26 + 65)
        else:
            decrypted_message += char
    for i in range(1, len(decrypted_message)+1):
        if ((i > 0) & (i % 5 == 0)):
            print(decrypted_message[i-1] + " " , end='')
        elif((i % 50 == 0) & (i > 0)):
            print (decrypted_message[i-1] + "\n")
        else:
            print(decrypted_message[i-1], end='')
    return ""
#example: message = "Hello Friends to you me"
#shift = 1
message = file.read()
print (message + "\n")
shift = int(sys.argv[1])
decrypted_message = decrypt_caesar(message.replace(" ", ""), shift)
print(decrypted_message)
