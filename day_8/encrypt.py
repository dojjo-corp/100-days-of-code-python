alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# Don't change the code above
#########################################################
# function to encrypt text
#def encrypt(plain_text, shift_number):
#    shift_index = []
#    encrypted_word = ""
#    for letter in text:
#        letter_index = alphabets.index(letter)
#        letter_index += shift
#        letter_index %= 26
#        encrypted_word += alphabets[letter_index]
    
#    print(f"The encoded text is {encrypted_word}")

# function to decrypt text
#def decrypt(cipher_text, shift_number):
#    decrypted_word = ""
#    for letter in cipher_text:
#        letter_index = alphabets.index(letter)
#        letter_index = abs(letter_index - shift)
#        letter_index %= 26
#        decrypted_word += alphabets[letter_index]
#    print(f"Your decoded text is {decrypted_word}")
#######################################################3

def caesar(text, shift, direction):
    # to hold the final result
    result = ""
    # to hold index of letter in alphabet list
    alpha_position = 0
    # to hold letter position after operation performed
    new_position = 0
    for letter in text:
        # for whitespaces
        if letter not in alphabets:
            result += letter
            continue
        # get hold of index of letter in alphabets list
        alpha_position = alphabets.index(letter)
        if direction == "encode":
            # for encoding, shift letter position to the right
            new_position = alpha_position + shift
            new_position %= 26
        elif direction == "decode":
            # for decoding, shift letter position to the left
            new_position = alpha_position - shift
            new_position %= 26
        result += alphabets[new_position]
    print(f"The final output is:\n{result}")
    
# to check if user wants to quit
is_end = False

while is_end == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    response = input("Would like to go again? (yes/no)\n")
    if response == "no":
        print("Goodbye!")
        is_end = True
    elif response != "yes":
        print("Enter the right thing for once in your miserable life!")
        is_end = True
