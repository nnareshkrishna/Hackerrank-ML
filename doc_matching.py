import json
stops=['i' , 'me' , 'my' , 'myself' , 'we' , 'our' , 'ours' , 'ourselves' , 'you' , 'your' , 'yours' , 'yourself' , 'yourselves' , 'he' , 'him' , 'his' , 'himself' , 'she' , 'her' , 'hers' , 'herself' , 'it' , 'its' , 'itself' , 'they' , 'them' , 'their' , 'theirs' , 'themselves' , 'what' , 'which' , 'who' , 'whom' , 'this' , 'that' , 'these' , 'those' , 'am' , 'is' , 'are' , 'was' , 'were' , 'be' , 'been' , 'being' , 'have' , 'has' , 'had' , 'having' , 'do' , 'does' , 'did' , 'doing' , 'a' , 'an' , 'the' , 'and' , 'but' , 'if' , 'or' , 'because' , 'as' , 'until' , 'while' , 'of' , 'at' , 'by' , 'for' , 'with' , 'about' , 'against' , 'between' , 'into' , 'through' , 'during' , 'before' , 'after' , 'above' , 'below' , 'to' , 'from' , 'up' , 'down' , 'in' , 'out' , 'on' , 'off' , 'over' , 'under' , 'again' , 'further' , 'then' , 'once' , 'here' , 'there' , 'when' , 'where' , 'why' , 'how' , 'all' , 'any' , 'both' , 'each' , 'few' , 'more' , 'most' , 'other' , 'some' , 'such' , 'no' , 'nor' , 'not' , 'only' , 'own' , 'same' , 'so' , 'than' , 'too' , 'very' , 's' , 't' , 'can' , 'will' , 'just' , 'don' , 'should' , 'now']
def score(s1,s2):
	a=s1.split(' ')
	b=s2.split(' ')
	le=len(b)
	wa={}
	wb={}
	for i in a:
		i=i.lower()
		if(i not in stops):
			if(i not in wa):
				wa[i]=1 
			else:
				wa[i]=wa[i]+1

	for i in b:
		if(i not in stops):
			if(i not in wb):
				wb[i]=1
			else:
				wb[i]=wb[i]+1

	score=0
	for i in a:
		i=i.lower()
		if(i in wb):
			temp= wa[i]*wb[i]*(1.0/tc[i])
			score = score + temp

	score = score * 1.0 / le
	return score

def score1(s1,s2):
	a=s1.split(' ')
	b=s2.split(' ')
	le=len(b)
	wa={}
	wb={}
	for i in a:
		i=i.lower()
		if(i not in stops):
			if(i not in wa):
				wa[i]=1 
			else:
				wa[i]=wa[i]+1

	for i in b:
		if(i not in stops):
			if(i not in wb):
				wb[i]=1
			else:
				wb[i]=wb[i]+1

	score=0
	for i in a:
		i=i.lower()
		if(i in wb):
			temp= wa[i]*wb[i]*(1.0/tc[i])
			score = score + temp

	#score = score * 1.0 / le
	return score



def func(para,q,ans):
	fans=[0 for i in range(0,5)]
	tans=['' for i in range(0,5)]
	ct=0
	for i in range(0,len(ans)):
		s=ans[i]
		max=0
		#index=''
		index=0
		for j in range(0,len(para)):
			temp=score(s,para[j])
			if(temp>max):
				max=temp
				index=j
		
		#print para[index]
		tans[i]=index

	for i in range(0,5):
		max=0
		index=0
		for j in range(0,5):
			temp=score1(q[i],para[tans[j]])
			if(temp>max):
				max=temp
				index=j
			
		fans[i]=index

	for i in range(0,5):
		temp=fans[i]
		print ans[temp]


tc={}
s=raw_input()
para=s.split('.')
q=['' for i in range(0,5)]
for i in range(0,5):
	s=raw_input()
	q[i]=s
#print ;
s=raw_input()
ans=s.split(';')
index=[i for i in range(0,5)]

for i in para:
	s=i.split(' ')
	for j in s:
		j=j.lower()
		if(j not in stops):
			if(j not in tc):
				tc[j]=1 
			else:
				tc[j]=tc[j]+1

func(para,q,ans)
print ;
#for i in range(0,5):
#	print ans[i]
#for i in ans:
#	print i
#print ;