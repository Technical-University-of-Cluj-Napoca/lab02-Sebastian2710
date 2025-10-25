from collections import defaultdict

def group_anagrams (strings: list[str]) -> list[list[str]]:
    d = defaultdict(list)
    for s in strings:
        count = [0]*26
        for c in s:
            count[ord(c) - ord('a')] +=1
        key=tuple(count)
        d[key].append(s)
    return d.values()

strs = ["eat","tea","tan","bat","ate","nat"]
strs2 = [""]
strs3 = ["a"]

print(group_anagrams(strs))
print(group_anagrams(strs2))
print(group_anagrams(strs3))

