from pathlib import Path
import struct
path = Path("gamepwn_sokobanhtb/out/build/x64-release/SokobanHTB/SokobanHTB.exe")
data = path.read_bytes()
base = 0x1400b8e80 - 0x140000000
chunk = data[base:base+256*4]
ints = list(struct.unpack("<256I", chunk))
for row in range(16):
    print(ints[row*16:(row+1)*16])
