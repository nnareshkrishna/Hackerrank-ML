import math
def func(xm,ym,x2m,y2m,xy,n):
	res=0.0
	res = n * xy
	res = res - (xm * ym)
	den = 0.0
	den = ((n * x2m) - (xm ** 2) ) * ((n * y2m) - (ym ** 2))
	den = den **0.5
	res = res / den
	return res

n=input()
x=[0 for j in range(0,n)]
y=[0 for j in range(0,n)]
z=[0 for j in range(0,n)]
for i in range(0,n):
	b=raw_input()
	b1=b.split('	')
	x[i]=int(b1[0])
	y[i]=int(b1[1])
	z[i]=int(b1[2])

#for i in range(0,n):
#	for j in range(0,3):
#		print a[i][j],
#	print ;

xi=0;yi=0;zi=0;
for i in range(0,n):
	xi = xi + x[i]
	yi = yi + y[i]
	zi = zi + z[i]

x2=0;y2=0;z2=0;
for i in range(0,n):
	x2 = x2 + (x[i]**2) 
	y2 = y2 + (y[i]**2)
	z2 = z2 + (z[i]**2)

xy=0;yz=0;xz=0 ;
for i in range(0,n):
	xy = xy + (x[i]*y[i])
	yz = yz + (y[i]*z[i])
	xz = xz + (x[i]*z[i])

rxy = func(xi,yi,x2,y2,xy,n)
ryz = func(yi,zi,y2,z2,yz,n)
rxz = func(xi,zi,x2,z2,xz,n)

print ("%.2f" % rxy)
print ("%.2f" % ryz)
print ("%.2f" % rxz)