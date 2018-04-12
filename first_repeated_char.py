def firstRepeatedChar(str):


    seen = {}
    for char in str:
        if char in seen:
            return char
        else:
            seen[char] = 0

    return 


print firstRepeatedChar("cnbcbayyarea")
