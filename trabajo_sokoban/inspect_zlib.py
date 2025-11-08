import zlib
path = 'gamepwn_sokobanhtb/out/build/x64-release/SokobanHTB/SokobanHTB.exe'
with open(path, 'rb') as f:
    data = f.read()
positions = [i for i in range(len(data)-2) if data[i] == 0x78 and data[i+1] in (0x01, 0x9c, 0xda, 0x5e)]
for pos in positions[:10]:
    print('pos', hex(pos))
    success = False
    for wbits in (15, -15):
        try:
            obj = zlib.decompressobj(wbits)
            out = obj.decompress(data[pos:])
            unused = len(obj.unused_data)
            preview = out[:60]
            print('  wbits', wbits, 'len', len(out), 'unused', unused)
            print('   preview', preview)
            success = True
            break
        except Exception as e:
            print('  wbits', wbits, 'error', e)
    if not success:
        print('  failed')
