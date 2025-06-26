def group_by_first_letter(words):
    grouped = {}
    for word in words:
        first = word[0]
        if first not in grouped:
            grouped[first] = []
        grouped[first].append(word)
    return grouped
words = ["apple", "ant", "banana", "bat", "cat"]
print(group_by_first_letter(words))
# print(grouped)