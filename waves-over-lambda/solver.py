import random
import math
import string
from collections import Counter
from wordfreq import zipf_frequency

cipher_text = """aynsbhur tebe zr wymb iqhs - ibejmenaw_zr_a_yceb_qhvdkh_kncuibuhwm\n-------------------------------------------------------------------------------\nge gebe nyu vmat vybe uthn h jmhbueb yi hn tymb ymu yi ymb rtzf uzqq ge rhg teb rznl, hnk uten z mnkebruyyk iyb ute izbru uzve gthu ghr vehnu dw h rtzf iymnkebzns zn ute reh.  z vmru halnygqekse z thk thbkqw ewer uy qyyl mf gten ute rehven uyqk ve rte ghr rznlzns; iyb ibyv ute vyvenu uthu utew bhuteb fmu ve znuy ute dyhu uthn uthu z vzstu de rhzk uy sy zn, vw tehbu ghr, hr zu gebe, kehk gzutzn ve, fhbuqw gzut ibzstu, fhbuqw gzut tybbyb yi vznk, hnk ute utymstur yi gthu ghr weu deiybe ve."""

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

def decrypt_with_key(key):
    table = str.maketrans(ALPHABET, key)
    return cipher_text.translate(table)

word_cache = {}

def word_score(word):
    if word in word_cache:
        return word_cache[word]
    if not word:
        score = 0.0
    else:
        score = zipf_frequency(word, 'en')
    word_cache[word] = score
    return score


def score_text(plaintext):
    total = 0.0
    for token in plaintext.lower().split():
        clean = ''.join(ch for ch in token if ch.isalpha())
        if clean:
            total += word_score(clean)
    return total

best_key = initial_key
best_score = score_text(decrypt_with_key(best_key))

random.seed(0)

ITERATIONS = 100
STEPS = 6000
for iter_num in range(ITERATIONS):
    key_list = list(initial_key)
    random.shuffle(key_list)
    current_key = ''.join(key_list)
    current_plain = decrypt_with_key(current_key)
    current_score = score_text(current_plain)
    temp = 10.0
    cooling = 0.999
    for _ in range(STEPS):
        a, b = random.sample(range(26), 2)
        key_list = list(current_key)
        key_list[a], key_list[b] = key_list[b], key_list[a]
        new_key = ''.join(key_list)
        new_plain = decrypt_with_key(new_key)
        new_score = score_text(new_plain)
        delta = new_score - current_score
        if delta > 0 or math.exp(delta / temp) > random.random():
            current_key = new_key
            current_score = new_score
            current_plain = new_plain
            if current_score > best_score:
                best_score = current_score
                best_key = current_key
        temp *= cooling
        if temp < 0.001:
            temp = 0.001
    if (iter_num + 1) % 10 == 0:
        print(f"Iteration {iter_num+1}: current={current_score:.2f}, best={best_score:.2f}")

print("Best key:", best_key)
print(decrypt_with_key(best_key))
