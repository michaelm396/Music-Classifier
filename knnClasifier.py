import math

class point:
    def __init__(self):
        self.coords = []
        self.classification = ""

def euclidean_distance(p1,p2):
    totalSum = 0
    for i in range(len(p1)):
        totalSum += pow(p1[i]-p2[i],2)
    return math.sqrt(totalSum)



"""
train and test are a list of lists, where each list is a series of float coordinates
i.e. x,y,z,etc. followed by a class (string)
"""
def knn(train,test,k):
    #take in train data into list of classes
    parsedTrain = []
    for i in range(len(train)):
        p = point()
        p.classification = train[i][len(train[i])-1]
        p.coords = train[i][:len(train[i])-1]
        parsedTrain += [p]

    correctNumber = 0
    totalNumber = len(test)
    outputList = []

    for i in range(len(test)):
        currPoint = test[i][:len(test[i])-1]
        currClass = test[i][len(test[i])-1] #for error calculation

        #construct a dictionary mapping classes to the closest k points for that class
        classToKdistances = dict()
        for p in parsedTrain:
            #calculate euclidean distance beween two points
            dist = euclidean_distance(currPoint,p.coords)
            #update classToKdistances mainatining sorted arrays
            if p.classification in classToKdistances:
                if (len(classToKdistances[p.classification]) < k):
                    idx = 0
                    L = classToKdistances[p.classification]
                    while (idx < len(L) and dist < L[idx]):
                        idx += 1
                    classToKdistances[p.classification] = L[:idx] + [dist] + L[idx:]
                else:
                    L = classToKdistances[p.classification]
                    if dist < L[0]:
                        idx = 1
                        while (idx < len(L) and dist < L[idx]):
                            idx += 1
                        classToKdistances[p.classification] = L[1:idx] + [dist] + L[idx+1:]
            else:
                classToKdistances[p.classification] = [dist]

        #find closest class to this point
        bestSum = None
        bestClass = None
        for c in classToKdistances:
            currSum = sum(classToKdistances[c])
            if (bestSum == None or currSum < bestSum):
                bestSum = currSum
                bestClass = c

        #if it's correctly classified record it
        if bestClass == currClass:
            correctNumber += 1

        outputList += [(currClass,bestClass)]

    print(correctNumber/totalNumber)
    return outputList


#testTrain = [[0,1,1,"A"],[0,2,1,"A"],[5,5,1,"B"],[4,6,1,"B"],[1,2,1,"B"],[4,4,1,"A"]]
#testTest = [[0,0,1,"A"],[7,7,1,"B"],[3,3,1,"A"]]
#print(knn(testTrain,testTest,2))















