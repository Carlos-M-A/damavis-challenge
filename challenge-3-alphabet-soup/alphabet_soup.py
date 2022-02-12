"""Alphabet soup

    Author: Carlos-M-A

    The funtion to use is is_this_message_in_the_alphabet_soup.
"""

def count_letters(string):
    """It counts the amount of each letter in the string.

    Args:
        string (str): The string about making the counting

    Returns:
        dic: Dictionary with the letter counting
    """
    counting = {}
    for letter in string:
        letter = letter.lower()
        if not letter in "abcdefghijklmnñopqrstuvwxyz":
            continue
        if letter in counting:
            counting[letter] = counting[letter] + 1
        else:
            counting[letter] = 1
    return counting

def is_this_message_in_the_alphabet_soup(wanted_message, letters_in_soup):
    """It checks if is possible make the wanted message with the letters in the
       alphabet soup.

       This function only works with ascii letters (uppercase and lowercase) plus
       the ñ letter (abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ).
       This do not work with diacritics. You must to remove the diacritics of the
       letters in the two arguments before you use this function.

       Args:
           wanted_message (str): The complete message which you want to make with
                                 the letters in the alphabet soup
           letters_in_soup (str): The complete list of letters in the alphabet soup

       Returns:
           bool: True if the wanted message is possible. False if not.
    """
    letter_counting_in_wanted_message = count_letters(wanted_message)
    letter_counting_in_alphabet_soup = count_letters(letters_in_soup)

    for letter, counting in letter_counting_in_wanted_message.items():
        letter = letter.lower()
        if not letter in letter_counting_in_alphabet_soup:
            return False
        if letter_counting_in_wanted_message[letter] > letter_counting_in_alphabet_soup[letter]:
            return False

    return True
