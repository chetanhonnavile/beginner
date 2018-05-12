# accept the string and k
# then break the string into len(string)/k parts
# print each part with no repeated characters in the original order

def merge_the_tools(string, k):
    j = k
    i = 0
    for _ in range(len(string)):
        res = string[i:j]
        i += k
        j += k
        res = list(res)
        print "".join(p for p in sorted(set(res),key=res.index))
        
        if j > len(string):
            break
            
            
print merge_the_tools('AABCDCCED', 3)
