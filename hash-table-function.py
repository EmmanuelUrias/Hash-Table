hash_table = {
    'march 6': 200,
    'march 7': 202,
    'march 8': 209,
    'march 9': 203,
}


def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


print(get_hash('march 9'))
