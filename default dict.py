from collections import defaultdict
sequences_A = [(23, 24, 22, 44),(325, 353, 554), (24354, 353, 325), (2454, 353, 325)]
sequences_B = [('23', '24','22', '44'),('325', '351', '554'), ('24354', '353', '325'), ('2454', '353', '325')]
pairs = defaultdict(lambda : defaultdict( int))

for (words, tags) in zip(sequences_A, sequences_B):
    for w, t in zip(words, tags):
        if w in pairs.keys() and t in pairs[w].keys():
            pairs[w][t] += 1
        else:
            pairs[w][t] = 1

mfc_table = {}
for tag, words in pairs.items():
    for word, freq in words.items():
        if word in mfc_table.keys():
            if pairs[mfc_table[word]][word] < freq:
                mfc_table[word] = tag
        else:
            mfc_table[word] = tag


_dict = defaultdict(int)
for sentence in sequences_A:
    for tag in sentence:
        _dict[tag] += 1


