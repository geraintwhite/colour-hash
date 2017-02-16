import hash
import sys


if (len(sys.argv) < 2):
    data = sys.stdin.buffer.read()
else:
    data = bytes(' '.join(sys.argv[1:]), 'utf-8')

if data == '-h' or data == '--help':
    print('Usage: python main.py sometext')
else:
    out = hash.colour_hash(data)
    print('\n'.join(''.join(i*2 for i in row) for row in hash.chunks(out, 8)))
