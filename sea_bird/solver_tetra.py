import random
import math
import string
from collections import Counter, defaultdict
from pathlib import Path

CT = (b"tliHwc6D5\x02w+Xw;5<.pgoX\x11w%XwUXC<DQ\x02X\x03w\x1b.gw.yw,.\x085wvDpX\x03w\x08Q+XyXD\x1bX+w&<\x1bow[w\x16tw&<Q2\x03w\x05<vvX2\x1bw\x02.pgX\x1b<\x1b<.Qw<2w2XDw\x05<5+w\x05\x08\x1bw<\x1bw2XXp2wC<:Xw,.\x08woD)XwDwv..+w\x02oDQ\x02Xw.yw&<QQ<Qv\x11w<\x02\x1byjy5XQ\x02o~o.52X2~+X2X5)X~p.5X~C.)X~\x1b.. wUD\x02Xw2\x1bD5\x1b2wDQ+w\x1boD\x1bwC\x08QD\x1b<\x02w2XDw\x05<5+w)XX52w.yyw<Q\x1b.w\x1boXwyD5w\x02.5QX5wDQ+w<2w\x1b5DggX+w2.pX&oX5Xw<Qw\x1boXwp<++CXw.yw\x1boXwgD\x02:\x11wL.\x08wpDQDvXw\x1b.w\x1bD:Xw\x1boXwCXD+wD\x1bw\x1boXw\x1boXwy<QDCw\x02.5QX5\x03wgCXQ\x1b,w.ywXQX5v,w<pg.22<\x05CXw\x1b.wC.2XwQ.&\x11\x11\x11w%\x08\x1bw.\x08\x1bw.ywQ.&oX5Xw\x02.pX2w2XDw\x05<5+w\x11\x11\x11w&o.w\x1boXQw\x05XD\x1b2w,.\x08w\x05,wiwCXQv\x1bo2\x1e\x04\x1ew\x07CD\x02XwuQ+w\x05XD\x1b<Qvw\x1bo<5+w\x05,wDQ.\x1boX5wHwCXQv\x1bo2\x11wR.wXp\x05D55D22X+w\x1boD\x1bw,.\x08w5X\x1b<5Xw<ppX+<D\x1bXC,\x11")

unique = sorted(set(CT))
index = {b: i for i, b in enumerate(unique)}
data = [index[b] for b in CT]
counts = Counter(data)

candidate_chars = list(dict.fromkeys(
    string.ascii_letters + string.digits + " {}_.,;:!?()-'\"[]/@#%&*\\\n"
))

if len(candidate_chars) < len(unique):
    raise SystemExit("Not enough candidate characters")

initial_chars = candidate_chars[:len(unique)]
extra_chars = candidate_chars[len(unique):]

corpus_path = Path("corpus.txt")
if not corpus_path.exists():
    raise SystemExit("Missing corpus.txt for language model")

corpus = corpus_path.read_text(encoding="utf-8", errors="ignore").lower()
allowed = "".join(candidate_chars)
filtered = "".join(ch for ch in corpus if ch in allowed)

if len(filtered) < 1000:
    raise SystemExit("Corpus too small after filtering")

tetra_counts = defaultdict(int)
for i in range(len(filtered) - 3):
    gram = filtered[i:i + 4]
    tetra_counts[gram] += 1

total = sum(tetra_counts.values())
floor = math.log(0.01 / total)
tetra_scores = {g: math.log(c / total) for g, c in tetra_counts.items()}

random.seed()


def decode(mapping):
    return "".join(mapping[idx] for idx in data)


def score_text(text):
    score = 0.0
    for i in range(len(text) - 3):
        gram = text[i:i + 4]
        score += tetra_scores.get(gram, floor)
    score += text.count("ictf") * 400.0
    score += text.count("{") * 40.0
    score += text.count("}") * 40.0
    score += text.count(" the ") * 20.0
    return score


symbol_order = sorted(range(len(unique)), key=lambda i: -counts[i])

best_score = float("-inf")
best_mapping = None
best_text = ""

restarts = 80
steps = 120000

for restart in range(restarts):
    mapping = ["?"] * len(unique)
    chars = initial_chars.copy()
    random.shuffle(chars)
    for symbol, ch in zip(symbol_order, chars):
        mapping[symbol] = ch
    unused_chars = [c for c in initial_chars if c not in mapping]
    iterator = iter(unused_chars)
    for i in range(len(mapping)):
        if mapping[i] == "?":
            mapping[i] = next(iterator, " ")
    unused_pool = extra_chars.copy()
    random.shuffle(unused_pool)
    current_text = decode(mapping)
    current_score = score_text(current_text)
    temperature = 6.0
    for step in range(steps):
        temperature = max(0.001, temperature * 0.9995)
        proposal = mapping.copy()
        proposal_unused = unused_pool.copy()
        if random.random() < 0.75 or not proposal_unused:
            i, j = random.sample(range(len(proposal)), 2)
            proposal[i], proposal[j] = proposal[j], proposal[i]
        else:
            i = random.randrange(len(proposal))
            new_char = random.choice(proposal_unused)
            proposal_unused.remove(new_char)
            proposal_unused.append(proposal[i])
            proposal[i] = new_char
        proposal_text = decode(proposal)
        proposal_score = score_text(proposal_text)
        delta = proposal_score - current_score
        if delta > 0 or math.exp(delta / temperature) > random.random():
            mapping = proposal
            unused_pool = proposal_unused
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
print("MAPPING:")
print("".join(best_mapping))
