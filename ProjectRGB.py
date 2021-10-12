def rgb1(r,g,b):
    def limit(p):
            if p<0: return 0
            if p>255: return 255
            return p
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
def rgb2(r, g, b):
    limit = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (limit(r), limit(g), limit(b))
print(rgb1(-20, 275, 125))
print(rgb2(-20, 275, 125))