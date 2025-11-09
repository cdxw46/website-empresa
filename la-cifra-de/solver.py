import random
import math
import string
from collections import Counter
import enchant
from wordfreq import zipf_frequency, top_n_list

with open('cipher.txt', 'r', encoding='utf-8-sig') as f:
    lines = f.read().strip().splitlines()

if lines and lines[0].lower().startswith('encrypted message'):
    lines = lines[1:]

cipher_text = '\n'.join(lines).strip()

ALPHABET = string.ascii_lowercase
FREQ_ORDER = "etaoinshrdlcumwfgypbvkxqjz"

letters = [c for c in cipher_text.lower() if c in ALPHABET]
freq = Counter(letters)
ordered_cipher = ''.join([item[0] for item in freq.most_common()])
ordered_cipher += ''.join([c for c in ALPHABET if c not in ordered_cipher])

initial_key_map = {c: p for c, p in zip(ordered_cipher, FREQ_ORDER)}


def fill_missing(mapping):
    mapping = dict(mapping)
    used = set(mapping.values())
    unused = [c for c in ALPHABET if c not in used]
    for c in ALPHABET:
        if c not in mapping:
            mapping[c] = unused.pop(0)
    return ''.join(mapping[c] for c in ALPHABET)

initial_key = fill_missing(initial_key_map)


def decrypt_with_key(key: str) -> str:
    table = str.maketrans(ALPHABET, key)
    return cipher_text.translate(table)


en_dict = enchant.Dict('en_US')
word_cache = {}
COMMON_WORDS = set(top_n_list('en', n=20000))


def word_score(word: str) -> float:
    if word in word_cache:
        return word_cache[word]
    if not word:
        score = 0.0
    else:
        score = zipf_frequency(word, 'en')
    word_cache[word] = score
    return score


def score_text(plaintext: str) -> float:
    total = 0.0
    for token in plaintext.lower().split():
        clean = ''.join(ch for ch in token if ch.isalpha())
        if clean:
            total += word_score(clean)
            if clean in COMMON_WORDS:
                total += 15.0
            if en_dict.check(clean):
                total += 8.0
    return total


def random_key() -> str:
    letters = list(ALPHABET)
    random.shuffle(letters)
    return ''.join(letters)


best_key = initial_key
best_plain = decrypt_with_key(best_key)
best_score = score_text(best_plain)
current_key = best_key
current_score = best_score
start_temp = 30.0
min_temp = 0.001
cooling = 0.9995
temperature = start_temp

TOTAL_STEPS = 2000000
REPORT_EVERY = 100000
RESTART_EVERY = 200000

for step in range(1, TOTAL_STEPS + 1):
    a, b = random.sample(range(26), 2)
    key_list = list(current_key)
    key_list[a], key_list[b] = key_list[b], key_list[a]
    new_key = ''.join(key_list)
    new_plain = decrypt_with_key(new_key)
    new_score = score_text(new_plain)
    delta = new_score - current_score
    if delta > 0 or math.exp(delta / temperature) > random.random():
        current_key = new_key
        current_score = new_score
        if current_score > best_score:
            best_score = current_score
            best_key = current_key
            best_plain = new_plain
    temperature *= cooling
    if temperature < min_temp:
        temperature = min_temp
    if step % REPORT_EVERY == 0:
        print(f"Paso {step}: score={current_score:.2f}, mejor={best_score:.2f}")
    if step % RESTART_EVERY == 0:
        current_key = random_key()
        current_score = score_text(decrypt_with_key(current_key))
        temperature = start_temp

print("Mejor clave:", best_key)
print(best_plain)
