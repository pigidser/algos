# k, l = map(int, input().split())

# enc_letters = dict()
# for i in range(k):
#     letter, code = input().split(': ')
#     enc_letters.setdefault(letter, code)

# encoded_str = input()
# assert len(encoded_str) == l

k, l = 4, 14
enc_letters = {'a': '0', 'b': '10', 'c': '110', 'd': '111'}
encoded_str = '01001100100111'
assert len(encoded_str) == l

code_letters = {enc_letters[key]: key for key in enc_letters}

i, decoded_str = 0, ''
while i < len(encoded_str):
    window_len = 1
    while encoded_str[i:i+window_len] not in code_letters:
        window_len += 1
    decoded_str = decoded_str + code_letters[encoded_str[i:i+window_len]]
    i += window_len

print(decoded_str)