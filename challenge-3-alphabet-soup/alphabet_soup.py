"""Alphabet soup

    Author: Carlos-M-A

    The funtion to use is is_this_message_in_the_alphabet_soup.
"""

def count_letters(string):
    """It counts the amount of each letter in the string.
        Performance:
            n = length of string
            T(n) = O(n)
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

       Performance:
           m = length of wanted_message
           s = length of letters_in_soup
           Best case 1 (soup smaller than message): T(m, s) = 1 < O(1)
           Best case 2 (message is in the soup): T(m, s) = m + s/2 (On average) < O(m + s)
           Worst case (message is not in the soup): T(m, s) = m + s < O(m + s)

       Args:
           wanted_message (str): The complete message which you want to make with
                                 the letters in the alphabet soup
           letters_in_soup (str): The complete list of letters in the alphabet soup

       Returns:
           bool: True if the wanted message is possible. False if not.
    """
    if len(wanted_message) > len(letters_in_soup):
        return False
    if len(wanted_message) == 0:
        return True

    letter_counting_in_wanted_message = count_letters(wanted_message)

    for letter in letters_in_soup:
        letter = letter.lower()
        if not letter in letter_counting_in_wanted_message:
            continue
        letter_counting_in_wanted_message[letter] -= 1
        if letter_counting_in_wanted_message[letter] == 0:
            del letter_counting_in_wanted_message[letter]

        if len(letter_counting_in_wanted_message) == 0:
            return True

    return False