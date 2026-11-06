import sys

if len(sys.argv) < 2:
    print("Usage: python3 caesar_brute.py 'SHIFTED TEXT'")
    sys.exit(1)

text = sys.argv[1].upper()

for key in range(1, 26):
    out = ''
    for c in text:
        if c.isalpha():
            out += chr((ord(c) - 65 - key) % 26 + 65)
        else:
            out += c
    print(f'Key {key:2d}: {out}')
