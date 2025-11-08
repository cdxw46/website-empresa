from pathlib import Path
with open("board_ascii.txt") as f:
    rows = [line.strip() for line in f if line.strip()]
map_chars = "".join(rows)
mapping = {".":0,"#":1,"x":2,"B":3,"P":4}
byte_pattern = bytes(mapping[ch] for ch in map_chars)
exe = Path("gamepwn_sokobanhtb/out/build/x64-release/SokobanHTB/SokobanHTB.exe").read_bytes()
idx = exe.find(byte_pattern)
print("found at", idx)
