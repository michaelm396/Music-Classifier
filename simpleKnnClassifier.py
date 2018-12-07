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
        #classToKdistances = dict()
        kNearestNeighbors = []
        for p in parsedTrain:
            #calculate euclidean distance beween two points
            dist = euclidean_distance(currPoint,p.coords)
            #update classToKdistances mainatining sorted array
            if (len(kNearestNeighbors) < k):
                #insert value into list
                idx = 0
                while (idx < len(kNearestNeighbors) and kNearestNeighbors[idx][0] > dist):
                    idx += 1
                kNearestNeighbors = kNearestNeighbors[:idx] + [(dist,p.classification)] + kNearestNeighbors[idx:]
            else:
                if (kNearestNeighbors[0][0] > dist):
                    #insert element and remove first elem
                    idx = 0
                    while (idx < len(kNearestNeighbors) and kNearestNeighbors[idx][0] > dist):
                        idx += 1
                    kNearestNeighbors = kNearestNeighbors[1:idx] + [(dist,p.classification)] + kNearestNeighbors[idx:]


        #find closest class to this point
        #create dict of class to points,total dist
        classToPoints = dict()
        for j in range(len(kNearestNeighbors)):
            if classToPoints.__contains__(kNearestNeighbors[j][1]):
                classToPoints[kNearestNeighbors[j][1]][0] += 1
                classToPoints[kNearestNeighbors[j][1]][1] += kNearestNeighbors[j][0]
            else:
                classToPoints[kNearestNeighbors[j][1]]= [1,kNearestNeighbors[j][0]]
        #pick class w/ most points, with dist as tie breaker
        bestClass = None
        bestTotalPoints = 0
        bestDist = None
        for c in classToPoints:
            currNumPoints = classToPoints[c][0]
            if currNumPoints > bestTotalPoints:
                bestTotalPoints = currNumPoints
                bestDist = classToPoints[c][1]
                bestClass = c
            elif currNumPoints == bestTotalPoints:
                if (classToPoints[c][1] < bestDist):
                    bestDist = classToPoints[c][1]
                    bestClass = c

        #if it's correctly classified record it
        if bestClass == currClass:
            correctNumber += 1

        outputList += [(currClass,bestClass)]
    pdb.set_trace()
    print(correctNumber/totalNumber)
    return outputList


#testTrain = [[0,1,1,"A"],[0,2,1,"A"],[5,5,1,"B"],[4,6,1,"B"],[1,2,1,"B"],[4,4,1,"A"]]
#testTest = [[0,0,1,"A"],[7,7,1,"B"],[3,3,1,"A"]]
#print(knn(testTrain,testTest,3))





