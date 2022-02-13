import pytest
import alphabet_soup

def test_count_letters_OK():
    counting = {'c':2, 'a':3, 't':1, 'u':1}
    result_lowercase_letters = alphabet_soup.count_letters('cacatua')
    assert counting == result_lowercase_letters

    result_capital_letters = alphabet_soup.count_letters('CACATUA')
    assert counting == result_capital_letters

    result_others_characters = alphabet_soup.count_letters('$CA%&CAT22309U333A')
    assert counting == result_others_characters

def test_is_this_message_in_the_alphabet_soup_OK():
    wanted_message_1 = 'queremos queso'
    letters_in_soup_1 = 'dijfgoqsueeurqemso'
    result_1 = alphabet_soup.is_this_message_in_the_alphabet_soup(wanted_message_1, letters_in_soup_1)
    assert result_1 == True

    wanted_message_2 = 'queremos queso'
    letters_in_soup_2 = 'oqsueeurqems'
    result_2 = alphabet_soup.is_this_message_in_the_alphabet_soup(wanted_message_2, letters_in_soup_2)
    assert result_2 == False

    wanted_message_3 = 'queremos queso'
    letters_in_soup_3 = 'ñlakjsdfqpoeuirghdasf'
    result_3 = alphabet_soup.is_this_message_in_the_alphabet_soup(wanted_message_3, letters_in_soup_3)
    assert result_3 == False