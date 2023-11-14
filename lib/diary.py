def make_snippet(word):
    word1 = word.split(" ")
    if len(word1) > 5:
        first_five = word1[:5]
        snippet = " ".join(first_five)
        return snippet + "..."
    else:
        return word
