def is_one_away_diff_lengths(s1,s2):
    i = 0
    count_diff = 0
    #print "2nd fun"
    #print "s1",s1
    #print "s2",s2
    while i < len(s2):

        if s1[i+count_diff] == s2[i]:
            #print s1[i+count_diff],":",s2[i]
            #print "s1[",i,"+",count_diff,"] == s2[",i,"]"

            i += 1
        else:
            count_diff += 1
            #print "count_diff",count_diff
            if count_diff > 1:
                #print count_diff
                return False
    return True

def is_one_away_same(s1,s2):
    count_diff = 0
    #print "s1", s1
    #print "s2", s2
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count_diff += 1
            if count_diff > 1:
                return False
    return True

def is_one_away(s1,s2):
    res = [0,1,-1]
    if len(s1) - len(s2) not in res:
        return False
    elif len(s1) - len(s2) == 0:
        return is_one_away_same(s1,s2)
    elif len(s1) > len(s2):
        return is_one_away_diff_lengths(s1,s2)
    else:
        return is_one_away_diff_lengths(s2,s1)







print is_one_away('abde','abcde')
