import string
import random

def generate_random_id(length=6):
    """Generate a random alphanumeric ID of specified length."""
    characters = string.ascii_letters + string.digits  # kombinasikan huruf dan angka
    return ''.join(random.choice(characters) for _ in range(length))