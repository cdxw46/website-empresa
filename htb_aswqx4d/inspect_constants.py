def main():
    vals = [0x2A239824, 0x8A73EA61, 0xBA3CBD99, 0xDDBDD50D,
            0xF3444305, 0x47272423, 0x1517DD9C, 0xB639B429]
    bytes_le = []
    bytes_be = []
    for v in vals:
        bytes_le.extend([(v >> (8 * i)) & 0xFF for i in range(4)])
        bytes_be.extend([(v >> (8 * i)) & 0xFF for i in reversed(range(4))])

    def to_ascii(byte_list):
        return ''.join(chr(b) if 32 <= b < 127 else '.' for b in byte_list)

    print("little endian", bytes_le)
    print("le ascii", to_ascii(bytes_le))
    print("big endian", bytes_be)
    print("be ascii", to_ascii(bytes_be))


if __name__ == "__main__":
    main()
