from simpleKnnClassifier import knn
from parseAudioFile import songToFeatures
import os
from sklearn.svm import SVC
import pdb
import logging
import csv

def main():
    #go through songs in data set and construct train and test lists

    train = []
    test = []
    #trainGenreList = os.listdir("Songs/train")
    TEST = open("TEST_DATA.csv")
    reader = csv.reader(TEST)
    test = list(reader)
 
    #testGenreList = os.listdir("Songs/test") 
    TRAIN = open("TRAINING_DATA.csv")
    reader2 = csv.reader(TRAIN)
    train = list(reader2)
    
    #pdb.set_trace()
    #print(test)
    #print(songToFeatures("Songs/pop/Single-Ladies.mp3","pop"))

    print(knn(train,test,6))

if __name__ == "__main__":
    main()
    #import timeit
    #setup = "from __main__ import main2"
    #LOG_FILE_NAME = "logfile_genre_classifyer2.log"
    #logging.basicConfig(filename = LOG_FILE_NAME,filemode = 'w+',level = logging.DEBUG,format = '%(asctime)s - %(levelname)s: %(message)s',\
                     #datefmt = '%m/%d/%Y %I:%M:%S %p')
    #logging.debug(timeit.timeit("main2()", setup=setup))
    #logging.debug("COMPLETE")
