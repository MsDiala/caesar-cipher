# pull req [https://github.com/MsDiala/caesar-cipher/pull/1]

# Overview

Your job will be to devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

But don’t stop there! You’ll also need to devise a way to decipher the encrypted message event when you do NOT have the key!

# Feature Tasks and Requirements
[]Create an encrypt function that takes in a plain text phrase and a numeric shift.
    - the phrase will then be shifted that many letters.
        - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’
    - shifts that exceed 26 should wrap around
        - E.g. encrypt(‘abc’,27) would return ‘bcd’
[]shifts that push a letter out or range should wrap around
    E.g. encrypt(‘zzz’,1) would return ‘aaa’
[]Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
[]create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
[]Devise a method for the computer to determine if code was broken with minimal human guidance.
# Implementation Notes
- In order to accomplish a certain task you’ll need access to a corpus of English words.
    - A search on something like python list of english words should get you going.
# User Acceptance Tests
The application must…
encrypt a string with a given shift
decrypt a previously encrypted string with the same shift
encryption should handle upper and lower case letters
encryption should allow non-alpha characters but ignore them, including white space
decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
refer to supplied unit tests.

# Stretch Goals
Research the Vigenère cipher
Find some examples of ROT13 encrypted punchlines, spoilers, etc.
Break the code for a message written in language other than English.


# My comments about this Lab 
What is Caesar Cipher?
Caesar Cipher is a type of substitution cipher, in which each letter in the plain text is replaced by another letter at some fixed positions from the current letter in the alphabet.

For example, if we shift each letter by three positions to the right, each of the letters in our plain text will be replaced by a letter at three positions to the right of the letter in the plain text.
Let us see this in action – let’s encrypt the text “HELLO WORLD” using a right shift of 3.

 The Caesar Cipher encryption rule can be expressed mathematically as:

c = (x + n) % 26
Where c is the encoded character, x is the actual character, and n is the number of positions we want to shift the character x by. We’re taking mod with 26 because there are 26 letters in the English alphabet.

Caesar Cipher in Python
Before we dive into defining the functions for the encryption and decryption process of Caesar Cipher in Python, we’ll first look at two important functions that we’ll use extensively during the process – chr() and ord().
It is important to realize that the alphabet as we know them, is stored differently in a computer’s memory. The computer doesn’t understand any of our English language’s alphabet or other characters by itself.

Each of these characters is represented in computer memory using a number called ASCII code (or its extension – the Unicode) of the character, which is an 8-bit number and encodes almost all the English language’s characters, digits, and punctuations.
For instance, the uppercase ‘A’ is represented by the number 65, ‘B’ by 66, and so on. Similarly, lowercase characters’ representation begins with the number 97.

As the need to incorporate more symbols and characters of other languages arose, the 8 bit was not sufficient, so a new standard – Unicode – was adopted, which represents all the characters used in the world using 16 bits.
ASCII is a subset of Unicode, so the ASCII encoding of characters remains the same in Unicode. That means ‘A’ will still be represented using the number 65 in Unicode.
Note that the special characters like space ” “, tabs “\t”, newlines “\n”, etc. are also represented in memory by their Unicode.

We’ll look at two built-in functions in Python that are used to find the Unicode representation of a character and vice-versa.

Encryption for Capital Letters
Now that we understand the two fundamental methods we’ll use, let’s implement the encryption technique for capital letters in Python. We shall encrypt only the uppercase characters in the text and will leave the remaining ones unchanged.
Let’s first look at the step-by-step process of encrypting the capital letters:

Define the shift value i.e., the number of positions we want to shift from each character.
Iterate over each character of the plain text:
If the character is upper-case:
Calculate the position/index of the character in the 0-25 range.
Perform the positive shift using the modulo operation.
Find the character at the new position.
Replace the current capital letter by this new character.
Else, If the character is not upper-case, keep it with no change.
Let us now look at the code:


shift = 3 # defining the shift count

text = "HELLO WORLD"

encryption = ""

for c in text:

    # check if character is an uppercase letter
    if c.isupper():

        # find the position in 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # perform the shift
        new_index = (c_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character

    else:

        # since character is not uppercase, leave it as it is
        encryption += c
        
print("Plain text:",text)

print("Encrypted text:",encryption)


# The Encryption Function
def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a') 

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

# The Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted
Now that we’ve defined our two functions let’s first use the encryption function to encrypt a secret message a friend is sharing via text message to his buddy.

plain_text = "Mate, the adventure ride in Canberra was so much fun, We were so drunk we ended up calling 911!"

ciphertext = cipher_encrypt(plain_text, 4)

print("Plain text message:\n", plain_text)

print("Encrypted ciphertext:\n", ciphertext)
