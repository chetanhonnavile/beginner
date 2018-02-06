def count_case(word):
        d = {"upper":0,"lower":0}
        for char in word:
                if char.isupper():
                        d["upper"]+=1
                elif char.islower():
                        d["lower"]+=1
                else:
                    pass

        print "original string:" ,word

        print "upper case:",d["upper"]
        print "lower case:",d["lower"]


count_case("The quICK Brown Fox")
