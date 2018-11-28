from simpleKnnClassifier import knn
from parseAudioFile import songToFeatures
import os

def main():
    #go through songs in data set and construct train and test lists

    train = []
    test = []
    genreList = os.listdir("Songs")
    for g in genreList:
        if (g != ".DS_Store"):
            genreSongs = os.listdir("Songs/"+g)
            for song in genreSongs:
                if (song != ".DS_Store"):
                    try:
                        L = songToFeatures("Songs/"+g+"/"+song,g)
                        test += [L]
                        train += [L]
                    except:
                        continue
    print(test)
    #print(songToFeatures("Songs/pop/Single-Ladies.mp3","pop"))

    print(knn(train,test,5))

if __name__ == "__main__":
    main()