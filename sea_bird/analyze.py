import ast
import json
from pathlib import Path

def decode(mapping):
    alphabet = mapping["alphabet"]
    trans = {alphabet[i]: mapping["mapping"][i] for i in range(len(alphabet))}
    ct = None
    for line in Path("sea_bird.py").read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith("#b"):
            ct = ast.literal_eval(stripped[1:])
            break
    if ct is None:
        raise ValueError("ciphertext not found")
    return ''.join(trans.get(chr(b), '?') for b in ct)

state = json.loads(Path("sa_best.json").read_text())
plaintext = decode(state)
print(plaintext)
letters = sorted(set(ch for ch in plaintext if ch.isalpha() and not ch.islower()))
print("Uppercase:", ''.join(letters))
from collections import Counter
counts = Counter(ch for ch in plaintext if ch.isalpha() and ch.isupper())
print("Counts:", counts)
for idx, ch in enumerate(plaintext):
    if ch.isalpha() and ch.isupper():
        segment = plaintext[max(0, idx-12):idx+13]
        print(f"{idx:4d}: {ch} -> {segment}")
