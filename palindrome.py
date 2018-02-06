def pali(word):
    start = 0
    end = len(word)-1
    while end >= start:
        if word[start] == word[end]:
            start += 1
            end -= 1
            return True
        return False



print pali(“epffpe”)
