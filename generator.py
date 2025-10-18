import random
from character_sets import get_character_sets

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    if not any([use_uppercase, use_lowercase, use_numbers, use_special]):
        return ""

    sets = get_character_sets()
    chars = set()
    required = []

    if use_lowercase:
        chars.update(sets['lowercase'])
        required.append(random.choice(sets['lowercase']))
    if use_uppercase:
        chars.update(sets['uppercase'])
        required.append(random.choice(sets['uppercase']))
    if use_numbers:
        chars.update(sets['digits'])
        required.append(random.choice(sets['digits']))
    if use_special:
        chars.update(sets['special'])
        required.append(random.choice(sets['special']))

    if len(required) > length:
        return "Length too short."

    all_chars = list(chars)
    password = required[:]
    for _ in range(length - len(required)):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

def evaluate_strength(password, prefs):
    score = 0
    import string

    if len(password) >= 12:
        score += 1
    if sum([prefs['uppercase'], prefs['lowercase'], prefs['numbers'], prefs['specials']]) >= 3:
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 3:
        return "Strong", "green"
    elif score == 2:
        return "Medium", "orange"
    else:
        return "Weak", "red"
