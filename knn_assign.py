	#Karthik V
#Assigment on Machine Learning to implemet weighted average knn 
#Opening a file

# W(Fever) = 0.3
# W(Vomitting) = 0.2
# W(Diarrhea) = 0.2
# W(Shivering) = 0.3

# no = 0 yes = 1 average = 2 high = 3

import math
import csv
import sys
import collections

#A function to return the corresponding values of association
def association(a,b):
	if(a=='no'and b=='no'):
		return 1.0
	elif(a=='no'and b=='average'):
		return 0.7
	elif(a=='no' and b=='high'):
		return 0.2
	elif(a=='average' and b=='no'):
		return 0.5
	elif(a=='average' and b=='avg'):
		return 1.0
	elif(a=='averge' and b=='high'):
		return 0.8
	elif(a=='high' and b=='no'):
		return 0.0
	elif(a=='high' and b=='average'):
		return 0.3
	elif(a=='high' and b=='high'):
		return 1.0
	else:
		return 0.0;

def csv_read():
	#data1 contains the csv file of the training data set
	f=open('data1.csv')
	csv_f=csv.reader(f)
	count=0 #to just keep a count of the rows traversed
		
	diction={}  # A dictionary to store the numeric association of the data
	diction['yes']=1
	diction['no']=0
	diction['average']=2
	diction['high']=3
	count=0
	temp=[]
	distance=[]
	man_distance=[]    #array to store the manhattan distances
	sim_value=[]  #array to store the similarity values
 	d={}   #dictionary to store the cluster corresponding to each Eucledian distance measure
	d1={}  #dictionary to store the cluster corresponding to the Manhattan values
	d2={}  #dictionary to store the cluster corresponding to the similarity values
	print 'Enter the input in the following order Fever(no/average/high),Vomitting(yes/no),Diarrhea(yes/no),Shivering(yes/no)'
	#x1=float(raw_input())
	#x2=float(raw_input())
	#x3=float(raw_input())
	#x4=float(raw_input())
	s1=raw_input()
	s2=raw_input()
	s3=raw_input()
	s4=raw_input()
	# Take the values in a Linguistic manner
	# Convert the linguistic input to numeric values using map
	x1=float(diction[s1])
	x2=float(diction[s2])
	x3=float(diction[s3])
	x4=float(diction[s4])
	i=0
	print 'data set'
	for row in csv_f:
		try:
			if(count>0):
				#print row[0],row[1],row[2],row[3],row[4],
				p1=diction[row[0]]
				p2=diction[row[1]]
				p3=diction[row[2]]
				p4=diction[row[3]]
				cluster=row[4]
				temp.insert(i,cluster)
				value = math.sqrt((0.3)*square(p1-x1) + (0.2)*square(p2-x2) +  (0.2)*square(p3-x3) + (0.3)*square(p4-x4))
				value1=(0.3*abs(p1-x1)+0.2*abs(p2-x2)+ 0.2*abs(p3-x3) + 0.3*abs(p4-x4))
				sum_val=0.3*association(s1,row[0]) + 0.2*association(s2,row[1]) + 0.2*association(s3,row[2])+0.3*association(s4,row[3]) #to find the total similarity
				distance.insert(i,value)
				man_distance.insert(i,value1)
				sim_value.insert(i,sum_val)
				d[value]=cluster
				d1[value1]=cluster
				d2[sum_val]=cluster
				i=i+1
		except IndexError :
			print 'Empty row'
		count=count+1
	#print distance,
	#print temp
	
	voting=[]
	distance.sort()
	c=collections.Counter()
	print '*************Calculation based on Eucledian distance*****************'
	print 'Eucledian distance vector :'
	print distance
	print 'Enter the k value'
	k=int(raw_input())
	min_val=distance[0]
	i=0
	for j in range(0,k):
		#insert all neighbours to the list
		voting.insert(i,d[distance[j]])
		i=i+1
	
	for word in voting:
		c[word]+=1
	print 'Most common:'
	for letter, count in c.most_common(1):
		char=letter
		print '%s: %7d' % (letter, count)

	if(char=='I'):
		print 'Disease Classification : Influenza'
	elif(char=='H'):
		print 'Disease Classification : Healthy'
	elif(char=='B'):
		print 'Disease Classification : Bowel Inflamation'
	elif(char=='S'):
		print 'Disease Classification : Salmonella Poisoning'
	else:
		print 'No Classification found'
	#Output of Manhattan Distance

	print '*************Calculation based on Manhatan distance*****************'
	idx=0
	man_voting=[]
	man_distance.sort()
	print 'Manhattan Distance Vector :'
	cnt=collections.Counter()
	print man_distance
	for j in range(0,k):
		#Insert all the neighbours on to the list for the voting
		man_voting.insert(idx,d1[man_distance[j]])
		idx=idx+1
	for word in man_voting:
		cnt[word]+=1
	
	print 'Most common:'
	for letter, count in cnt.most_common(1):
		char=letter
		print '%s: %7d' % (letter, count)

	if(char=='I'):
		print 'Disease Classification :Influenza'
	elif(char=='H'):
		print 'Disease Classification : Healthy'
	elif(char=='B'):
		print 'Disease Classification : Bowel Inflamation'
	elif(char=='S'):
		print 'Disease Classification : Salmonella Poisoning'
	else:
		print 'No Classification found'
	

	print '*************Calculation based on similarity measures****************'
	i=0
	sim_voting=[]
	sim_value.sort()
	sim_value.reverse()  #We need the descending order to get the most similar
	c1=collections.Counter() #This will store the value of each alphabet and the corresponding counter
	print sim_value

	#Voting is done by finding the most frequent character in the list
	
	for j in range (0,k):
		print d2[sim_value[j]],
		sim_voting.insert(i,d2[sim_value[j]])
		i=i+1

	for word in sim_voting:
		c1[word]+=1
	
	print 'Most common:'
	for letter, count in c1.most_common(1):
		char=letter
		print '%s: %7d' % (letter, count)

	if(char=='I'):
		print 'Disease Classification : Influenza'
	elif(char=='H'):
		print 'Disease Classification : Healthy'
	elif(char=='B'):
		print 'Disease Classification : Bowel Inflamation'
	elif(char=='S'):
		print 'Disease Classification : Salmonella Poisoning'
	else:
		print 'No Classification found'

	f.close()

def square(x):
	return x**2;  
print '****************************Assignment*************************'

csv_read()