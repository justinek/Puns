import sys, re, string

f = open(sys.argv[1], "r")

firstline = 0

toksDict = dict()

print "pairID,sentenceID,isCorrect,isPun,relatedness,order,wordOrder,condition,workderID,age,gender,native"

for l in f:
    l = l.replace("\n", "")
    l = l.replace('"', "")
    if firstline == 0:
        firstline = 1
        #labels = l.split(",")
    else:
        toks = l.split(",")
        workerID = toks[0]
        results = toks[1]
        wordOrders = toks[2]
        isCorrects = toks[3]
        isPuns = toks[4]
        orders = toks[5]
        age = toks[6]
        gender = toks[7]
        condition = toks[8]
        native = toks[9]
        pairID = toks[10]
        sentenceID = toks[11]
        
        
        pairIDs = pairID.split(";")
        sentenceIDs = sentenceID.split(";")
        isCorrectsToks = isCorrects.split(";")
        isPunsToks = isPuns.split(";")
        resultsToks = results.split(";")
        ordersToks = orders.split(";")
        wordOrdersToks = wordOrders.split(";")

        for i in range(len(ordersToks)):
            print pairIDs[i] + "," + sentenceIDs[i] + "," + isCorrectsToks[i] + "," + isPunsToks[i] + "," + resultsToks[i] + "," + ordersToks[i] + "," +wordOrdersToks[i] + "," + condition + "," + workerID + "," + age + "," + gender + "," + native    

            

