import hashlib
pw_bytes = b"i\x07\x01\x1f'o-5Ki;1i\x1bO8\x11O\x01O\x1e8KO\x01b.b5i\x0b\x01b\x0bi\x07\x018\x11q"
print(len(pw_bytes))
for name in ('md5','sha1','sha256'):
    h = getattr(hashlib, name)(pw_bytes).hexdigest()
    print(name, h)
for name in ('md5','sha1','sha256'):
    h = getattr(hashlib, name)(pw_bytes.hex().encode()).hexdigest()
    print(name, 'hexstr', h)
