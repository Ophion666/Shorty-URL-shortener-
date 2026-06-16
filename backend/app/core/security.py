import string, random

def generate_shorty_key(length: int = 6):
    characters = string.ascii_letters + string.digits

    random_chars = random.choices(characters, k = length)

    return "".join(random_chars)