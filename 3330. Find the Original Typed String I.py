class Solution:
  def possibleStringCount(self, word: str) -> int:

    groups = []
    i = 0
    while i < len(word):
        char = word[i]
        count = 1
        while i + 1 < len(word) and word[i + 1] == char:
            count += 1
            i += 1
        groups.append((char, count))
        i += 1

    possible = {word}

    for group_index in range(len(groups)):
        char, count = groups[group_index]
        if count > 1:
            for shorter in range(1, count):
                new_chunks = []
                for i in range(len(groups)):
                    c, n = groups[i]
                    if i == group_index:
                        new_chunks.append(c * shorter)
                    else:
                        new_chunks.append(c * n)
                new_word = ''.join(new_chunks)
                possible.add(new_word)

    return len(possible)