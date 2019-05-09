from knnCuda import knn
from parseAudioFile import songToFeatures
import os
import pdb

def main():
    #go through songs in data set and construct train and test lists

    train = []
    test = []
    
    TEST = open("TEST_DATA.csv")
    reader = csv.reader(TEST)
    test = list(reader)
    
    TRAIN = open("TRAINING_DATA.csv")
    reader2 = csv.reader(TRAIN)
    train = list(reader2)
    """
    trainGenreList = os.listdir("Songs/train")
    for g in trainGenreList:
        if (g != ".DS_Store"):
            genreSongs = os.listdir("Songs/train/"+g)
            for song in genreSongs:
                if (song != ".DS_Store"):
                    try:
                        L = songToFeatures("Songs/train/"+g+"/"+song,g)
                        train += [L]
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
                        test += [L]
                    except:
                        continue
    """
    print(test)
    #print(songToFeatures("Songs/pop/Single-Ladies.mp3","pop"))

    print(knn(train,test,6))

if __name__ == "__main__":
    main()
