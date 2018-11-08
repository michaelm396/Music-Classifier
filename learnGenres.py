from simpleKnnClassifier import knn

def main():
    #go through songs in data set and construct train and test lists
    train = [[0,1,1,"A"],[0,2,1,"A"],[5,5,1,"B"],[4,6,1,"B"],[1,2,1,"B"],[4,4,1,"A"]]
    test = [[0,0,1,"A"],[7,7,1,"B"],[3,3,1,"A"]]
    #run knn and output results
    print(knn(train,test,3))

if __name__ == "__main__":
    main()