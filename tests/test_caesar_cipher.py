import pytest

from caesar_cipher.caesar_cipher import encrypt, decrypt, crack



def test_decrypt_shift_20():
    actual = decrypt(encrypt("apple", 20),20)
    expected = "apple"
    assert actual == expected


def test_encrypt_very_large_shift():
    actual = encrypt("apple", 101)
    expected = "xmmib"
    assert actual == expected


def test_encrypt_negative_wrapping():
    actual = encrypt("apple", -3)
    expected = "xmmib"
    assert actual == expected



def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected


def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected


def test_encrypt_shift_20():
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected


def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected


def test_with_whitespace():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected


def test_with_non_alpha():
    actual = encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    assert actual == expected


def test_round_trip():
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected


