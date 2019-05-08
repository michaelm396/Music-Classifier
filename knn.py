# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:54:42 2019

@author: tt14r
"""
import operator
import torch
from torch.autograd import Variable, Function
import knn_pytorch
import numpy as np


"""
train and test are a list of lists, where each list is a series of float coordinates
i.e. x,y,z,etc. followed by a class (string)
"""
def knn(train,test,k):
    test_y=[]
    Train_class=[]
    Train_coords=[]
    Test_class=[]
    Test_coords=[]
    #take in train data into list of classes
    for i in range(len(train)):
        classification = train[i][len(train[i])-1]
        coords = train[i][:len(train[i])-1]
        Train_class += [classification]
        Train_coords += [coords]
    for i in range(len(test)):
        classification = train[i][len(train[i])-1]
        coords = train[i][:len(train[i])-1]
        Test_class += [classification]
        Test_coords += [coords]
    ref = Train_coords.float().cuda()
    query = Test_coords.float().cuda()

    inds = torch.empty(k, query.shape[1]).long().cuda()
    dists = torch.empty(k, query.shape[1]).float().cuda()

    knn_pytorch.knn(ref, query, inds, dists)
    
    for y in range(np.shape(inds,0)):
        classVotes = {}
        for x in range(np.shape(inds,1)):
            i=inds[y][x]
            response = Train_class[i]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        test_y[y]=sortedVotes[0][0]
        return test_y