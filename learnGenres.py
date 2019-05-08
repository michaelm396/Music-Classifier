from simpleKnnClassifier import knn
from parseAudioFile import songToFeatures
import os
import pdb
from sklearn.svm import SVC

def main():
    #go through songs in data set and construct train and test lists

    #train = []
    #test = []
    xTrain1 = []
    yTrain1 = []
    xTest1 = []
    yTest1 = []

    xTrain20 = []
    yTrain20 = []
    xTest20 = []
    yTest20 = []

    xTrain100 = []
    yTrain100 = []
    xTest100 = []
    yTest100 = []

    xTrain1000 = []
    yTrain1000 = []
    xTest1000 = []
    yTest1000 = []

    trainGenreList = os.listdir("Songs/train")
    for g in trainGenreList:
        if (g != ".DS_Store"):
            genreSongs = os.listdir("Songs/train/"+g)
            for song in genreSongs:
                if (song != ".DS_Store"):
                    try:
                        L = songToFeatures("Songs/train/"+g+"/"+song,g)
                        train += [L]
                        xTrain1 += [L[:len(L)-1]]
                        yTrain1 += [L[len(L)-1]]

                        xTrain20 += [L[:len(L)-1]]
                        yTrain20 += [L[len(L)-1]]

                        xTrain100 += [L[:len(L)-1]]
                        yTrain100 += [L[len(L)-1]]

                        xTrain1000 += [L[:len(L)-1]]
                        yTrain1000 += [L[len(L)-1]]
                        
                    except:
                        continue

    testGenreList = os.listdir("Songs/test") 
    for g in testGenreList:
        if (g != ".DS_Store"):
            genreSongs = os.listdir("Songs/test/"+g)
            for song in genreSongs:
                if (song != ".DS_Store"):
                    try:
                        L = songToFeatures("Songs/test/"+g+"/"+song,g)
                        #test += [L]
                        xTest1 += [L[:len(L)-1]]
                        yTest1 += [L[len(L)-1]]

                        xTest20 += [L[:len(L)-1]]
                        yTest20 += [L[len(L)-1]]

                        xTest100 += [L[:len(L)-1]]
                        yTest100 += [L[len(L)-1]]

                        xTest1000 += [L[:len(L)-1]]
                        yTest1000 += [L[len(L)-1]]
                    except:
                        continue

    print(test)
    #print(songToFeatures("Songs/pop/Single-Ladies.mp3","pop"))
    
    print(xTrain1)
    print(yTrain1)
    print(xTest1)
    svclassifier1 = SVC(kernel='rbf',C=1) #1,20,100,500,1000
    svclassifier1.fit(xTrain1,yTrain1)
    yPred1 = svclassifier1.predict(xTest1)
    resList1 = []
    correctNum1 = 0
    for i in range(len(yPred1)):
        resList1 += [(yTest1[i],yPred1[i])]
        if (yTest1[i] == yPred1[i]):
            correctNum1 += 1
    print(correctNum1/len(yPred1))
    print(resList1)


    print(xTrain20)
    print(yTrain20)
    print(xTest20)
    svclassifier20 = SVC(kernel='rbf',C=20) #1,20,100,500,1000
    svclassifier20.fit(xTrain20,yTrain20)
    yPred20 = svclassifier20.predict(xTest20)
    resList20 = []
    correctNum20 = 0
    for i in range(len(yPred20)):
        resList20 += [(yTest20[i],yPred20[i])]
        if (yTest20[i] == yPred20[i]):
            correctNum20 += 1
    print(correctNum20/len(yPred20))
    print(resList20)



    print(xTrain100)
    print(yTrain100)
    print(xTest100)
    svclassifier100 = SVC(kernel='rbf',C=100) #1,20,100,500,1000
    svclassifier100.fit(xTrain100,yTrain100)
    yPred100 = svclassifier100.predict(xTest100)
    resList100 = []
    correctNum100 = 0
    for i in range(len(yPred100)):
        resList100 += [(yTest100[i],yPred100[i])]
        if (yTest100[i] == yPred100[i]):
            correctNum100 += 1
    print(correctNum100/len(yPred100))
    print(resList100)



    print(xTrain1000)
    print(yTrain1000)
    print(xTest1000)
    svclassifier1000 = SVC(kernel='rbf',C=1000) #1,20,100,500,1000
    svclassifier1000.fit(xTrain1000,yTrain1000)
    yPred1000 = svclassifier1000.predict(xTest1000)
    resList1000 = []
    correctNum1000 = 0
    for i in range(len(yPred1000)):
        resList1000 += [(yTest1000[i],yPred1000[i])]
        if (yTest1000[i] == yPred1000[i]):
            correctNum1000 += 1
    print(correctNum1000/len(yPred1000))
    print(resList1000)

    #print(knn(train,test,7))

if __name__ == "__main__":
    main()
