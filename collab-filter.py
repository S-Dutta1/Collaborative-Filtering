import math
import csv
import ast
def de(a):
	d=map(lambda x:0 if(x==-1) else 1,a)
	return list(d)
def modf(a):
	d=map(lambda x:-x if(x<0) else x,a)
	return list(d)	
def pro(A,B):
	s=sum(list( map(lambda x,y:x*y if(x!=-1 and y!=-1) else 0, A,B)))
	return s
def mean(a):
	a=list(a);
	return sum(a)/len(a);	
def cov(a,b):
	a=list(a);
	b=list(b);
	p=map(lambda x,y:x*y, a,b)
	z=sum(p)/len(a)-mean(a)*mean(b);
	return z;
def function(A,B):
	a=list(filter(lambda x: x!=0, map(lambda x,y:x if(x!=-1 and y!=-1) else 0, A,B))) # this is done to take only insersection of a , b 
	b=list(filter(lambda x: x!=0, map(lambda x,y:y if(x!=-1 and y!=-1) else 0, A,B))) # that r none -1 
	if(cov(a,a)==0 or cov(b,b)==0):
		x=0
	else:
		x= cov(a,b)/(math.sqrt(cov(a,a)*cov(b,b)));

	return x;
def f1(a):
	a=map(lambda x:ast.literal_eval(x),a);
	return list(a);

with open('movie-ratings.csv', 'r') as f:
	reader = csv.reader(f)
	your_list = list(reader) 
with open('user_preference.csv','r') as f:
	reader = csv.reader(f)
	my_list =list(reader)

	
p=zip(* your_list)
p=list(p)



xd=[]
for c in range(1,len(p)):
	xd.append(  (p[c][0], (de(f1(p[c][1:])),f1(p[c][1:])) ) )

my=f1(my_list[1])
my1=my
z=[]

for c in range(1,len(your_list)):
	z.append(function(my,f1(your_list[c][1:])))

ap = list(zip(*my_list))

ad=[]
for c in range(0,len(xd)):
	ad.append( (  pro(xd[c][1][1],z)/pro(xd[c][1][0],modf(z)) ,   (xd[c][0],int(ap[c][1]))  ) ) 


ad.sort() #sort always according to first column


ap=list(map(lambda x:(x[1][0],x[1][1]),ad) )
sd=list(map(lambda x:x[0],filter(lambda x: x[1]==-1 ,ap)))


for c in range(0,min(3,len(sd))):
	print(sd[len(sd)-c-1])