import math

def compute_mean(x,n):
	ans = 0.00
	for i in range(0,n):
		ans = ans + x[i]

	ans = ans*1.00
	ans = ans / n
	return ans 

def compute_sd(x,n,mean):
	ans = 0.00
	for i in range(0,n):
		ans = ans + (x[i] - mean)**2

	ans = ans / n
	ans = ans**0.5
	return ans


def func(x,a,n):
	ans=0.00
	for i in range(0,n):
			ans = ans + (x[i]-a[i])**2

	return ans


t=input()
for i2 in range(0,t):
	n=input()
	p=raw_input()
	l=p.split(' ')
	a=[]

	for i in l:
			a.append(float(i))

	mean=compute_mean(a,n)
	sd=compute_sd(a,n,mean)
	if(sd!=0):
		for i in range(0,n):
				a[i] = (a[i] - mean) * 1.0 / sd

	x = [[0.00 for j in range(0,n)]for i in range(0,5)]
	for i in range(0,5):
		p=raw_input()
		l=p.split(' ')
		x1=[0.00 for j in range(0,n)]
		for j in range(0,n):
			x1[j]=float(l[j])
		mean=compute_mean(x1,n)
		sd=compute_sd(x1,n,mean)
		#print ;
		#print mean,sd ;
		#print m
		if(sd!=0):
			for j in range(0,n):
				x1[j] = (x1[j] - mean) / sd
		for j in range(0,n):
			x[i][j]=x1[j]
		#	print x[i][j],
		#print ;

	#for i in range(0,n):
	#	print a[i],
	#print ;
	#print ;
	#print ;
	#for i in range(0,5):
	#	for j in range(0,n):
	#		print x[i][j],
	#	print ;

	index=1
	val=1000000.00
	for i in range(0,5):
		temp = func(x[i],a,n)
	#	print temp,
		if(temp < val):
			val = temp
			index = i+1

	#print ;
	print index