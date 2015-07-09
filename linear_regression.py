import math
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


#for i in range(0,n):
#	for j in range(0,f):
#		print x[i][j],
#	print y[i]


#for i in range(0,t):
#	for j in range(0,f):
#		print x1[i][j],
#	print ;

th=[100 for i in range(0,f)]
#alpha=[0.03,0.1,0.33,1,3.33,10]
#for i in range(alpha):
#	print alpha[i],
#

alpha=0.001
#Repeat the below code iter number of times
for p in range(0,1000):
	c=[0 for i in range(0,n)]

	for i in range(0,n):
		temp=0 ;
		for j in range(0,f):
			temp=temp + (x[i][j]*th[j])
		c[i]=temp ;	

	for i in range(0,n):
		c[i]=c[i]-y[i]
		#print c[i], 

	#print ;
	j1=0 ;

	for i in range(0,n):
		j1 = j1 + c[i]  

	#print j1 ;
	for i in range(0,n):
		for j in range(0,f):
					temp=j1*x[i][j]*(alpha) ;
					temp = temp / n ;  
					#print temp,
					th[j] = th[j] - temp
	#print ;
	#for i in range(0,f):
	#	print th[i],
	#
	#print  ;


y1=[]
for i in range(0,t):
	temp=0
	for j in range(0,f):
		temp = temp + x1[i][j]*th[j] 
	y1.append(temp)

for i in range(0,t):
	print y1[i]

