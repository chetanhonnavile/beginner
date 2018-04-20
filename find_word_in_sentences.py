queries = ["pen eraser","pen","pen pink","green"]
sente = ['paper pen eraser', 'pen paper pink', 'paper pen desk']


for sentence in sente:

    for query in queries:

        if len(query.split(" ")) > 1:

            for j in range(len(query.split(" "))):

                if query.split(" ")[j] in sentence:

                    pass
                else:

                    break
            else:
                print query.split(" "),"FOUND IN--->",sentence
        else:
            if query in sentence:
                print query,"found in--->",sentence
            else:
                print query,"Not found anywhere","in--->",sentence
