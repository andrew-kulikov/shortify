from .models import Shortcut


ALPHABET = '0123456789qwertyuiopasdfghjklzxcvbnm'


def get_next_key():
    last_shortcut = Shortcut.objects.latest('id')
    if not last_shortcut:
        next_key = '0' * 7
    else:
        next_key = last_shortcut.short_link
    pos = -1
    while next_key[pos] == ALPHABET[-1]:
        pos -= 1
    next_key = list(next_key)
    next_key[pos] = ALPHABET[ALPHABET.find(next_key[pos]) + 1]
    next_key = ''.join(next_key)
    return next_key
