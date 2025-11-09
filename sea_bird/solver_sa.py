import math
import random
import re
import string
import json
import os
from collections import Counter
from pathlib import Path
from wordfreq import zipf_frequency

CT = (b"tliHwc6D5\x02w+Xw;5<.pgoX\x11w%XwUXC<DQ\x02X\x03w\x1b.gw.yw,.\x085wvDpX\x03w\x08Q+XyXD\x1bX+w&<\x1bow[w\x16tw&<Q2\x03w\x05<vvX2\x1bw\x02.pgX\x1b<\x1b<.Qw<2w2XDw\x05<5+w\x05\x08\x1bw<\x1bw2XXp2wC<:Xw,.\x08woD)XwDwv..+w\x02oDQ\x02Xw.yw&<QQ<Qv\x11w<\x02\x1byjy5XQ\x02o~o.52X2~+X2X5)X~p.5X~C.)X~\x1b.. wUD\x02Xw2\x1bD5\x1b2wDQ+w\x1boD\x1bwC\x08QD\x1b<\x02w2XDw\x05<5+w)XX52w.yyw<Q\x1b.w\x1boXwyD5w\x02.5QX5wDQ+w<2w\x1b5DggX+w2.pX&oX5Xw<Qw\x1boXwp<++CXw.yw\x1boXwgD\x02:\x11wL.\x08wpDQDvXw\x1b.w\x1bD:Xw\x1boXwCXD+wD\x1bw\x1boXw\x1boXwy<QDCw\x02.5QX5\x03wgCXQ\x1b,w.ywXQX5v,w<pg.22<\x05CXw\x1b.wC.2XwQ.&\x11\x11\x11w%\x08\x1bw.\x08\x1bw.ywQ.&oX5Xw\x02.pX2w2XDw\x05<5+w\x11\x11\x11w&o.w\x1boXQw\x05XD\x1b2w,.\x08w\x05,wiwCXQv\x1bo2\x1e\x04\x1ew\x07CD\x02XwuQ+w\x05XD\x1b<Qvw\x1bo<5+w\x05,wDQ.\x1boX5wHwCXQv\x1bo2\x11wR.wXp\x05D55D22X+w\x1boD\x1bw,.\x08w5X\x1b<5Xw<ppX+<D\x1bXC,\x11")

alphabet = sorted(set(CT))
index = {b: i for i, b in enumerate(alphabet)}
data = [index[b] for b in CT]
counts = Counter(data)

LOCKED = {
    ord('w'): ' ',
}
LOCKED_INDICES = {index[b]: ch for b, ch in LOCKED.items() if b in index}

candidate_chars = list(dict.fromkeys(
    " " + string.ascii_lowercase + string.ascii_uppercase + "{}_.,!?'-\"\n"
))

if len(candidate_chars) < len(alphabet):
    raise SystemExit("Not enough candidate characters")

corpus_path = Path("corpus.txt")
if not corpus_path.exists():
    raise SystemExit("Missing corpus.txt")

corpus_text = corpus_path.read_text(encoding="utf-8", errors="ignore").lower()
filtered_corpus = ''.join(ch for ch in corpus_text if ch.isalpha() or ch == ' ')

if len(filtered_corpus) < 1000:
    raise SystemExit("Corpus too small after filtering")

tetragram_counts = Counter()
for i in range(len(filtered_corpus) - 3):
    tetragram_counts[filtered_corpus[i:i + 4]] += 1

total_tetragrams = sum(tetragram_counts.values())
tetragram_floor = math.log(0.01 / total_tetragrams)
tetragram_scores = {gram: math.log(count / total_tetragrams) for gram, count in tetragram_counts.items()}

random.seed()


def decode(mapping):
    return ''.join(mapping[idx] for idx in data)


def score_text(text):
    lower = text.lower()
    score = 0.0
    for i in range(len(lower) - 3):
        gram = lower[i:i + 4]
        score += tetragram_scores.get(gram, tetragram_floor)
    words = re.findall(r"[a-z]+", lower)
    if words:
        word_score = sum(max(zipf_frequency(w, "en"), -9.0) for w in words)
        score += 6.0 * word_score
    score += text.count("ictf{") * 4000.0
    brace_penalty = text.count("{") + text.count("}")
    score -= 15.0 * max(0, brace_penalty - text.count("ictf{") * 2)
    unwanted = "0123456789_/;:()[]!?\"-"
    for ch in unwanted:
        score -= 60.0 * text.count(ch)
    lowercase_bonus = sum(1 for ch in text if 'a' <= ch <= 'z')
    score += 5.0 * lowercase_bonus
    uppercase_penalty = sum(1 for ch in text if 'A' <= ch <= 'Z')
    score -= 60.0 * uppercase_penalty
    score += text.count(".") * 20.0
    score += text.count(",") * 10.0
    score += text.count(" the ") * 40.0
    score -= lower.count("\n\n") * 50.0
    return score


sorted_symbols = sorted(range(len(alphabet)), key=lambda i: -counts[i])


def initial_mapping():
    mapping = ['?'] * len(alphabet)
    used = set()
    for idx, ch in LOCKED_INDICES.items():
        mapping[idx] = ch
        used.add(ch)
    freq_order = list(" etaoinshrdlcumfpgwybvkxjqz")
    freq_chars = (freq_order +
                  list(string.ascii_lowercase) +
                  list(string.ascii_uppercase) +
                  list("{}_,.!?'-\""))
    freq_iter = iter(freq_chars)
    for symbol in sorted_symbols:
        if symbol in LOCKED_INDICES:
            continue
        next_char = next(freq_iter, None)
        while next_char is not None and next_char in used:
            next_char = next(freq_iter, None)
        if next_char is None:
            break
        mapping[symbol] = next_char
        used.add(next_char)
    for symbol in range(len(mapping)):
        if mapping[symbol] == '?':
            for ch in candidate_chars:
                if ch not in used:
                    mapping[symbol] = ch
                    used.add(ch)
                    break
    return mapping


def ensure_mapping(mapping):
    mapping = mapping.copy()
    used = set()
    available = [ch for ch in candidate_chars]
    for idx in range(len(mapping)):
        if idx in LOCKED_INDICES:
            locked_char = LOCKED_INDICES[idx]
            mapping[idx] = locked_char
            used.add(locked_char)
            if locked_char in available:
                available.remove(locked_char)
            continue
        ch = mapping[idx]
        if ch in candidate_chars and ch not in used:
            used.add(ch)
            if ch in available:
                available.remove(ch)
        else:
            if not available:
                ch = random.choice(candidate_chars)
            else:
                ch = available.pop(0)
            mapping[idx] = ch
            used.add(ch)
    return mapping


STATE_FILE = Path("sa_best.json")
saved_mapping = None
saved_score = None
if STATE_FILE.exists():
    try:
        state = json.loads(STATE_FILE.read_text())
        if state.get("alphabet") == ''.join(chr(c) for c in alphabet):
            saved_mapping = state.get("mapping")
            saved_score = state.get("score")
    except json.JSONDecodeError:
        saved_mapping = None
        saved_score = None

restarts = int(os.getenv("SA_RESTARTS", "3"))
steps = int(os.getenv("SA_STEPS", "8000"))

best_score = float("-inf")
best_mapping = None
best_text = ""

modifiable_indices = [idx for idx in range(len(alphabet)) if idx not in LOCKED_INDICES]

for restart in range(restarts):
    if restart == 0 and saved_mapping:
        mapping = ensure_mapping(saved_mapping)
    else:
        mapping = ensure_mapping(initial_mapping())
    current_text = decode(mapping)
    current_score = score_text(current_text)
    temperature = 7.0
    for step in range(steps):
        if not modifiable_indices:
            break
        temperature = max(0.001, temperature * 0.9993)
        i, j = random.sample(modifiable_indices, 2)
        proposal = mapping.copy()
        proposal[i], proposal[j] = proposal[j], proposal[i]
        proposal_text = decode(proposal)
        proposal_score = score_text(proposal_text)
        delta = proposal_score - current_score
        if delta > 0 or math.exp(delta / temperature) > random.random():
            mapping = proposal
            current_text = proposal_text
            current_score = proposal_score
    if current_score > best_score:
        best_score = current_score
        best_mapping = mapping.copy()
        best_text = current_text
        print(f"Restart {restart} score {best_score:.2f}")
        print(best_text[:200])

print("BEST SCORE", best_score)
print(best_text)

if best_mapping and best_score > (saved_score or float("-inf")):
    STATE_FILE.write_text(json.dumps({
        "alphabet": ''.join(chr(c) for c in alphabet),
        "mapping": best_mapping,
        "score": best_score,
        "plaintext": best_text[:5000],
    }, ensure_ascii=False, indent=2))
