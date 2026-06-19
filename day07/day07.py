def sqr(num):
    return num*num

sqr(7)
sqr(1024)

#over 1 score 6 : over 2 score 12 : over 3 score 18

def get_score(over):
    return over * 6

#over 1 score 8 : over 2 score 14 : over 3 score 20

def get_score(over):
    return over *6+2

score=[6,12,18]
score_2D=[[6],[12],[18]]

import numpy as np
#print (np)
over = np.array([[1],[2],[3],[4],[5]])
#over = np.array([[1],[2],[3],[4],[5],[10],[50],[100]])
#scores = np.array([6,12,18,30])
scores = np.array([8,14,20,26,32])
#scores = np.array([1,4,9,25])
#scores = np.array([1,4,9,16,25,100,2500,10000])
#print(over.shape)
#print(scores.shape)

from sklearn.linear_model import LinearRegression
#print(LinearRegression)

model=LinearRegression().fit(over,scores)
guess=int(model.predict([[6]])[0])
print(guess)