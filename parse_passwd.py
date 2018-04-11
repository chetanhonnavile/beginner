#parse the passwd file and print out the users and its ids.

out = {}
with open("passwd","r") as fd:

        for line in fd:
                user,id = line.strip("\n").split(":")[0],line.strip("\n").split(":")[2]
                if user in out:
                        out[user].append(id)
                else:
                        out[user] = []
                        out[user].append(id)
for i,j in out.items():
        print "user",i,"contains id(s) -->",j   
