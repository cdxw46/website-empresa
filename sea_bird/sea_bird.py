from Crypto.Util.number import long_to_bytes,bytes_to_long
from Crypto.Random import random


def affine(pt,key1,key2):
    if key1 == 0:
        key1 = 1
    return b''.join(long_to_bytes((key2 + key1 * i) % 128) for i in pt)

def xor(pt,key):
    return b''.join(long_to_bytes(i ^ key) for i in pt)


message = b'REDACTED'

for i in range(1000):
    k1,k2,k3 = random.getrandbits(7),random.getrandbits(7),random.getrandbits(7)

    message = affine(xor(message,k1),k2 | 1,k3)

print(message)
#b'tliHwc6D5\x02w+Xw;5<.pgoX\x11w%XwUXC<DQ\x02X\x03w\x1b.gw.yw,.\x085wvDpX\x03w\x08Q+XyXD\x1bX+w&<\x1bow[w\x16tw&<Q2\x03w\x05<vvX2\x1bw\x02.pgX\x1b<\x1b<.Qw<2w2XDw\x05<5+w\x05\x08\x1bw<\x1bw2XXp2wC<:Xw,.\x08woD)XwDwv..+w\x02oDQ\x02Xw.yw&<QQ<Qv\x11w<\x02\x1byjy5XQ\x02o~o.52X2~+X2X5)X~p.5X~C.)X~\x1b.. wUD\x02Xw2\x1bD5\x1b2wDQ+w\x1boD\x1bwC\x08QD\x1b<\x02w2XDw\x05<5+w)XX52w.yyw<Q\x1b.w\x1boXwyD5w\x02.5QX5wDQ+w<2w\x1b5DggX+w2.pX&oX5Xw<Qw\x1boXwp<++CXw.yw\x1boXwgD\x02:\x11wL.\x08wpDQDvXw\x1b.w\x1bD:Xw\x1boXwCXD+wD\x1bw\x1boXw\x1boXwy<QDCw\x02.5QX5\x03wgCXQ\x1b,w.ywXQX5v,w<pg.22<\x05CXw\x1b.wC.2XwQ.&\x11\x11\x11w%\x08\x1bw.\x08\x1bw.ywQ.&oX5Xw\x02.pX2w2XDw\x05<5+w\x11\x11\x11w&o.w\x1boXQw\x05XD\x1b2w,.\x08w\x05,wiwCXQv\x1bo2\x1e\x04\x1ew\x07CD\x02XwuQ+w\x05XD\x1b<Qvw\x1bo<5+w\x05,wDQ.\x1boX5wHwCXQv\x1bo2\x11wR.wXp\x05D55D22X+w\x1boD\x1bw,.\x08w5X\x1b<5Xw<ppX+<D\x1bXC,\x11'

