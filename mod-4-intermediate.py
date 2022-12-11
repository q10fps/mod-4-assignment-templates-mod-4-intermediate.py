'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "
    
    letter_ascii = ord(letter)
    letter_ascii += shift
    
    if letter_ascii > ord('z'):
        letter_ascii -= 26
    elif letter_ascii < ord('a'):
        letter_ascii += 26

    shifted_letter = chr(letter_ascii)
    return shifted_letter

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    encrypted_message = ""
    
    message = message.upper()
  
    encrypted_message = ""

    for char in message:

        if char.isalpha():
            ascii_code = ord(char)
            ascii_code += shift
            if ascii_code > ord('Z'):
                ascii_code -= 26
            elif ascii_code < ord('A'):
                ascii_code += 26
            encrypted_char = chr(ascii_code)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    letter = letter.lower()
    letter_shift = letter_shift.lower()
  
    ascii_code = ord(letter)
    ascii_code += ord(letter_shift) - ord('a')
    if ascii_code > ord('z'):
        ascii_code -= 26
    elif ascii_code < ord('a'):
        ascii_code += 26
    shifted_letter = chr(ascii_code)
    
    shifted_letter = shifted_letter.upper()
    return shifted_letter

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    key = ''.join(c for c in key.lower() if c.isalpha())
  
  # Extend the keyphrase to match the length of the message
    key *= len(message) // len(key)
    key += key[:(len(message) - len(key)) % len(key)]

    print("Message:", message)
    print("Key:", key)
    
    encrypted_message = ""
  
  # Loop over the characters in the message
    for i, c in enumerate(message):
    # Ignore characters that are not letters
        if not c.isalpha():
            encrypted_message += c
            continue
      
        ascii_code = ord(c)
        ascii_code += ord(key[i]) - ord('a')
        if ascii_code > ord('z'):
            ascii_code -= 26
        elif ascii_code < ord('a'):
            ascii_code += 26
        shifted_letter = chr(ascii_code)
    
        encrypted_message += shifted_letter
    return encrypted_message