with open('trainingdata.txt','r') as f :
	file=[]
	for l in f:
		file.append(l) 


t1=file[0]
t2=t1.split(' ')
t=int(t2[0])

#from nltk.corpus import stopwords									#For stopword removal
#stops=stopwords.words('english')
stops=['i' , 'me' , 'my' , 'myself' , 'we' , 'our' , 'ours' , 'ourselves' , 'you' , 'your' , 'yours' , 'yourself' , 'yourselves' , 'he' , 'him' , 'his' , 'himself' , 'she' , 'her' , 'hers' , 'herself' , 'it' , 'its' , 'itself' , 'they' , 'them' , 'their' , 'theirs' , 'themselves' , 'what' , 'which' , 'who' , 'whom' , 'this' , 'that' , 'these' , 'those' , 'am' , 'is' , 'are' , 'was' , 'were' , 'be' , 'been' , 'being' , 'have' , 'has' , 'had' , 'having' , 'do' , 'does' , 'did' , 'doing' , 'a' , 'an' , 'the' , 'and' , 'but' , 'if' , 'or' , 'because' , 'as' , 'until' , 'while' , 'of' , 'at' , 'by' , 'for' , 'with' , 'about' , 'against' , 'between' , 'into' , 'through' , 'during' , 'before' , 'after' , 'above' , 'below' , 'to' , 'from' , 'up' , 'down' , 'in' , 'out' , 'on' , 'off' , 'over' , 'under' , 'again' , 'further' , 'then' , 'once' , 'here' , 'there' , 'when' , 'where' , 'why' , 'how' , 'all' , 'any' , 'both' , 'each' , 'few' , 'more' , 'most' , 'other' , 'some' , 'such' , 'no' , 'nor' , 'not' , 'only' , 'own' , 'same' , 'so' , 'than' , 'too' , 'very' , 's' , 't' , 'can' , 'will' , 'just' , 'don' , 'should' , 'now']
#from nltk.stem.lancaster import LancasterStemmer					#For stemming
#st=LancasterStemmer()

total=t
#print t2
wc=[{}for i in range(0,9)]
tc={}
ct=[0 for i in range(0,9)]
while(t>0):
	n=file[total+1-t]
	a=n.split(' ')
	n1=int(a[0])
	ct[n1]=ct[n1]+1
#	print n1
	for j in range(1,len(a)):
		s=a[j].lower()
		#s=st.stem(s1)
		if(s not in wc[n1]):
			wc[n1][s]=1
		else:
			wc[n1][s]=wc[n1][s]+1
		if(s not in tc):
			tc[s]=1
		else:
			tc[s]=tc[s]+1
	t=t-1

#for i in range(1,9):
#		print ct[i]

x=input()
while(x>0):
	n=raw_input()
	a=n.split(' ')
	#print a
	fans=0.00
	index=1
	ans=1.00
	temp=1.00
	for i in range(1,9):
			ans=1
			temp=1.00
			ans=1.00
			for j in a:
				#print j,
				if(j not in stops):
					if(j not in wc[i]):
						if(j not in tc):
							temp=1.0/8
						else:
								temp=1.0/(tc[j]+8)
					else:
						temp=(wc[i][j]*1.0)
						temp=temp/(tc[j])

					ans=ans*temp
					ans=ans*10
	
			ans=(ans*ct[i])
			ans=ans/total
			#print i,ans
			if(ans>fans):
				fans=ans
				index=i
	print index
	x=x-1 

#for i,j in wc[2].items():
#		print i,j
#for i in range(0,9):
#	print i,ct[i]
