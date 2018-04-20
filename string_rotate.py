#are the 2 given strings rotatable

def str_rotat(str1,str2):

    if len(str1) != len(str2) and set(str1) != set(str2):
        return 0

    temp = str1+str1
    if temp.count(str2)>0:
        return 1
    else:
        return 0

if str_rotat("ABAECD","CDABAE"):
    print "strings are rotatable"
else:
    print "string are not rotatable"
