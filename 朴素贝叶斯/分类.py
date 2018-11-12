# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
# def trainB(trainM,trainLebel):
#     trainM=pd.DataFrame()
#     n_prop=trainM.shape
def trainB(trainM,labelCol,testLabel):
    n = trainM.shape[0]
    p_in = 1 / n
    n_f=trainM.shape[1]
    p_dict={}
    labels=trainM[labelCol]
    for prop in trainM:
        if prop!=labelCol:
            p_dict0={}
            for i,x in enumerate(trainM[prop]):
                if labels[i]==testLabel:
                    if x in p_dict0.keys():
                        p_dict0[x] += p_in
                    else:
                        p_dict0[x] = p_in
            p_dict[prop]=p_dict0
    return p_dict
if __name__ == '__main__':
    trainM = pd.DataFrame({"X1": [1] * 5 + [2] * 6 + [3] * 5,
                           "X2": ['S', 'L', 'M', 'M', 'S', 'L', 'S', 'S', 'L', 'L', 'M', 'M', 'L', 'S', 'M', 'M'],
                           "Label":[-1,1,1,-1,-1,1,1,-1,1,-1,1,1,1,1,-1,1]})
    p_dict1=trainB(trainM,"Label",1)
    p_dict2 = trainB(trainM, "Label", -1)
    a=1