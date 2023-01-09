import random
import string


def random_password():
    """
    This function make random password
    :return: string
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(6))
    return password


def random_email():
    """
    This function make random email
    :return: string
    """
    characters = string.ascii_letters
    email = ''.join(random.choice(characters) for i in range(6))
    return email + "@gmail.com"


def random_phone():
    """
    This function make random phone
    :return: string
    """
    number = string.digits
    phone = ''.join(random.choice(number) for i in range(7))
    return "+38050" + phone


def random_name():
    """
    This function make random name
    :return: string
    """
    characters = string.ascii_letters
    name = ''.join(random.choice(characters) for i in range(10))
    return name


def random_value():
    """
    This function make random value.
    Its fuction used for generate
    random values for incorrect inserts
    :return: string
    """
    characters = string.ascii_letters + string.digits
    value = ''.join(random.choice(characters) for i in range(6))
    return value
