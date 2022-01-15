import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = [(freq, i, Leaf(ch)) for i, (ch, freq) in enumerate(Counter(s).items())]
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count, left = heapq.heappop(h)
        freq2, _count, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    # print(h)
    if h:
        [(_freq, _count, root)] = h
        # print(root)
        # print(type(root))
        root.walk(code, "")
    return code


def huffman_decode(encoded, code):
    code_letters = {code[key]: key for key in code}
    i, decoded = 0, ''
    while i < len(encoded):
        window_len = 1
        while encoded[i:i+window_len] not in code_letters:
            window_len += 1
        decoded = decoded + code_letters[encoded[i:i+window_len]]
        i += window_len
    return decoded


def main():
    s = input()
    code = huffman_encode(s)
    print(code)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f"{ch}: {code[ch]}")
    print(encoded)


def test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, 32)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = ''.join(code[ch] for ch in s)
        assert huffman_decode(encoded, code) == s
    print(f"All {n_iter} tests passed!")


if __name__ == "__main__":
    test()