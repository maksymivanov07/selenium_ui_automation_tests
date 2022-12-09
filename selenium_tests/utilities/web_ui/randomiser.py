import random
import string


def random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(6))
    return password


def random_email():
    characters = string.ascii_letters + string.digits + string.punctuation
    email = ''.join(random.choice(characters) for i in range(6))
    return email + "@gmail.com"


def random_phone():
    number = random.randrange(7)
    phone = "38050" + str(number)
    return phone
