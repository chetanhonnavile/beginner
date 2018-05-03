def rem_rep(word):

    # convert string to list
    word = list(word)
    i = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            del word[i]
            del word[i]
            i = 0
            if len(word) == 0:
                return "Empty String"
        else:
            i += 1

    return "".join(word)


print rem_rep('daabbe')
