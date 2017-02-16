import hashlib
import colours


def hash(data):
    return hashlib.sha512(data).digest()


def chunks(l, n=1):
    return (l[i:i+n] for i in range(0, len(l), n))


def colour_hash(data):
    out = []
    for b in chunks(hash(data)):
        h = sum(i for i in b)
        c = colours.hsv_to_rgb(h / 256, 1, 1)
        out.append(colours.colour_str(' ', bg=colours.rgb(*c)))
    return out
