# Author: Clara Hunt
# Github username: huntcl
# Date: 05/27/26
# Description: Counts how many times each letter appears in a string.

def count_letters(text):
    counts = {}
    for char in text:
        char = char.upper()
        if char >= "A" and char <= "Z":
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts
