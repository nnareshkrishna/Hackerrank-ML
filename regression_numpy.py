import math
import numpy as np
from sklearn import linear_model,datasets
q=raw_input()
w=q.split(' ')
f=int(w[0])
n=int(w[1])
x=[[0.00 for i in range(0,f)]for j in range(0,n)]
y=[0.00 for i in range(0,n)]

for i in range(0,n):
	q=raw_input()
	w=q.split(' ')
	for j in range(0,f):
		x[i][j]=float(w[j])
	y[i]=float(w[f])

t=input()
x1=[[0 for i in range(0,f)]for j in range(0,t)]
for i in range(0,t):
	q=raw_input()
	w=q.split(' ')
	for j in range(0,f):
		x1[i][j]=float(w[j])

model=linear_model.LinearRegression()
model.fit(x,y)

result=model.predict(x1)
#result.tolist()

for i in range(0,t):
	print result[i]