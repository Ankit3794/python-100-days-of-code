import art

print(art.logo)

should_end = False

while not should_end:
    operation = input("Type 'encode' to encrypt and 'decode' to decrypt message\n")
    if operation.lower() == 'encode':
        message = input('Type your message:\n')
        shift = int(input('Type the shift number:\n'))
        encode_msg = "".join([chr(ord(i)+shift) for i in message])
        print(encode_msg)
    elif operation.lower() == 'decode':
        message = input('Type your message:\n')
        shift = int(input('Type the shift number:\n'))
        decode_msg = "".join([chr(ord(i)-shift) for i in message])
        print(decode_msg)
    else:
        print("Please select proper option!!")
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")