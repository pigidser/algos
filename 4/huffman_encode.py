input_str = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus eligendi illum iste omnis voluptatum. Aspernatur atque, aut autem culpa dolorem eveniet hic illum neque nesciunt, officiis possimus repudiandae voluptate voluptatem!"
assert len(input_str) > 0

# Sort our string alphabetically and create a list where each element is also list (letter and its frequency)
s = sorted(input_str)
node_freq = [[s[0], 1]]
for i in range(1, len(s)):
    if s[i] != node_freq[-1][0]:    # if letter changes
        node_freq.append([s[i], 0])
    node_freq[-1][1] += 1

node_freq = sorted(node_freq, key=lambda x: x[1], reverse=True)
unique_letters = ''.join(map(lambda x: x[0], node_freq))
tree =  dict()

if len(node_freq) == 1:
    tree.setdefault('root' , [node_freq[0][0], None])

else:
    # Build binary tree
    while len(node_freq) > 1:
        # find left and right leafs of a node (they have the smallest frequency)
        i = len(node_freq) - 1
        while node_freq[i][1] > node_freq[i - 1][1]:
            i -= 1
        right = node_freq.pop(i)
        i = len(node_freq) - 1
        while node_freq[i][1] > node_freq[i - 1][1]:
            i -= 1
        left = node_freq.pop(i)
        # define a new node and insert it instead of the two with the lowest frequency 
        new_node = [left[0] + right[0], left[1] + right[1]]
        node_freq.insert(i, new_node)
        # add to the tree a node with its left/right childrens
        tree.setdefault('root' if len(node_freq) == 1 else new_node[0], [left[0], right[0]])

        node_freq = sorted(node_freq, key=lambda x: x[1], reverse=True)

        print(node_freq)

    print(tree)

def get_code(tree, node, letter, code):

    # check if left of right leaf of the node is our letter
    if letter in tree[node]:
        return code + str(tree[node].index(letter))

    # check which of leafs consists the letter
    for leaf in tree[node]:
        if letter in leaf:
            code = str(tree[node].index(leaf)) + get_code(tree, leaf, letter, code)

    return code


# Build a dictionary of encoded letters and encode the input string
enc_letters = dict()
for letter in unique_letters:
    enc_letters.setdefault(letter, get_code(tree, 'root', letter, ''))

encoded_str = ''.join([enc_letters[letter] for letter in input_str])

print(f"{len(unique_letters)} {len(encoded_str)}")
for letter in unique_letters:
    print(f"{letter}: {enc_letters[letter]}")
print(encoded_str)