def decrypt_caesar(message, shift):
    #message = " ".join(message.split())
    decrypted_message = ""
    for char in message.upper():
        if char.isalpha():
            shift_value = -shift
            if char.islower():
                decrypted_message += chr((ord(char) - 97 + shift_value) % 26 + 97)
            else:
                decrypted_message += chr((ord(char) - 65 + shift_value) % 26 + 65)
        else:
            decrypted_message += char
    for i in range(1, len(decrypted_message)):
        #decrypted_message.replace(" ", "")
        if ((i > 0) & (i % 6 == 0)):
            #& (i != 10)
            print(" ", end='')
        #elif (i == 11):
            #print(" ", end='')
        elif((i % 50 == 0) & (i > 0)):
            print (decrypted_message[i-1] + "\n")
        else:
            print(decrypted_message[i-1], end='')
    return ""
encrypted_message = "Hello Friends to you me"
shift = 1
decrypted_message = decrypt_caesar(encrypted_message.replace(" ", ""), shift)
