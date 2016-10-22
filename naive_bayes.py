# Karthik V
# Program to implement Naive Bayes classification
import collections
import math

count_clusters=0
fo=open("trainingdata.txt","r+")
array_cluster=[]
i=0
dict_word_map={}
# we create 8 list to put all the word count associations into that list
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
for row in fo.readlines():
	data=row.split()
	try:
		val=0  # This is an indicator variable to show which is the current class
		if(data[0].isdigit()):
			# print 'The data values ',
			count_clusters=count_clusters+1
			array_cluster.insert(i,data[0])  # array cluster contains different cluster values
			word_count = data[1].split(':')
			if(data[0]=='1'):
				val=1
			elif(data[0]=='2'):
				val=2
			elif(data[0]=='3'):
				val=3
			elif(data[0]=='4'):
				val=4
			elif(data[0]=='5'):
				val=5
			elif(data[0]=='6'):
				val=6
			elif(data[0]=='7'):
				val=7
			#print 'Word is ', word_count[0],
			#print ' count is ', word_count[1]
		#	word_list=[word,count]
		#	dict_word_map=
			i=i+1
#		block=data[1].split(':')
	

	except IndexError :
		print 'Empty row'
	if(val==1):
		list1.append(data[1])
	elif(val==2):
		list2.append(data[1])
	elif(val==3):
		list3.append(data[1])
	elif(val==4):
		list4.append(data[1])
	elif(val==5):
		list5.append(data[1])
	elif(val==6):
		list6.append(data[1])
	elif(val==7):
		list7.append(data[1])


# We will just print different classes and the correspoding entries in each classes

print ' Different class values '
print 'class 1: ', list1
print ' '
print ' '
print 'class 2: ', list2
print ' '
print ' '
print 'class 3: ', list3
print ' '
print ' '
print 'class 4: ', list4
print ' '
print ' '
print 'class 5: ', list5
print ' '
print ' '
print 'class 6: ', list6
print ' '
print ' '
print 'class 7: ', list7
print ' '
print ' '
print '*****************************************************************************************'
print 'count :',
print count_clusters
print 'Total Number of Clusters :',
total_count=len(set(array_cluster))   # set displays unique values and hence we get the perfect cluster count
print total_count

# The above step completes the formatting of data and we have the words and corresponding counts in each class

# To display the number of elements in each cluster
prob_1=0;
c=collections.Counter()
for word in array_cluster:
	c[word]+=1
for letter, count in c.most_common(8):
	char=letter
	print '%s: %7d' % (letter, count)
	count = count/1.0
	if(letter=='0'):
		print count
		prob_0=float(count/count_clusters)
	elif (letter=='1'):
		prob_1=float(count/count_clusters)
	elif (letter=='2'):
		prob_2=float(count/count_clusters)
	elif (letter=='3'):
		prob_3=float(count/count_clusters)
	elif (letter=='4'):
		prob_4=float(count/count_clusters)
	elif (letter=='5'):
		prob_5=float(count/count_clusters)
	elif (letter=='6'):
		prob_6=float(count/count_clusters)
	elif (letter=='7'):
		prob_7=float(count/count_clusters)
	else:
		print 'nothing'

# printing probability of different clusters

print 'Prob_Cluster 1 :',
print float(prob_1)

print 'Prob_Cluster 2 :',
print float(prob_2)

print 'Prob_Cluster 3 :',
print float(prob_3)

print 'Prob_Cluster 4 :',
print float(prob_4)

print 'Prob_Cluster 5 :',
print float(prob_5)

print 'Prob_Cluster 6 :',
print float(prob_6)

print 'Prob_Cluster 7 :',
print float(prob_7)

# Now we go to the different lists and check the total no of words, no of distinct words and the dictionay for word map 

dict_list1={}
dict_list2={}
dict_list3={}
dict_list4={}
dict_list5={}
dict_list6={}
dict_list7={}
dict_list8={}
# initalize the total count in each list to 0
total_count_l1=total_count_l2=total_count_l3=total_count_l4=total_count_l5=total_count_l6=total_count_l7=0

# We will start with list 1

# List 1
word1=[]
for item in list1:
	word_count=item.split(':')

	word1.append(word_count[0])
	if(word_count[0] in dict_list1):
		dict_list1[word_count[0]]+=int(word_count[1])
	else:
		dict_list1[word_count[0]]=int(word_count[1])
	total_count_l1=total_count_l1+int(word_count[1])

# Let us try to print the dictionary list one values, Now finding the probability of each word in a list is an easy task

# Key values and probablity of each word to be in list 1
dict_prob_list1={}  # dictionary to store the probability associated with each word to be in list 1

'Printing the word and word count in class 1 '
 
for key,val in dict_list1.items():
	unique=float(len(set(word1)))  # This takes the count of unique words in class 1
	prob_value=float(float(val+1)/(total_count_l1+unique))   # This finds the probability of each word note laplace smoothing is done
	dict_prob_list1[key]=prob_value
	print "{} = {}".format(key, val)

print ' '




# List 2 
word2=[]
for item in list2:
	word_count=item.split(':')
	word2.append(word_count[0])
	if(word_count[0] in dict_list2):
		dict_list2[word_count[0]]+=int(word_count[1])
	else:
		dict_list2[word_count[0]]=int(word_count[1])
	total_count_l2=total_count_l2+int(word_count[1])

dict_prob_list2={}  # dictionary to store the probability associated with each word to be in list 1

'Printing the word and word count in class 2 '
 
for key,val in dict_list2.items():
	unique=float(len(set(word2)))  # This takes the count of unique words in class 1
	prob_value=float(float(val+1)/(total_count_l2+unique))
	dict_prob_list2[key]=prob_value
	print "{} = {}".format(key, val)

print ' '


# List 3
word3=[]
for item in list3:
	word_count=item.split(':')
	word3.append(word_count[0])
	if(word_count[0] in dict_list3):
		dict_list3[word_count[0]]+=int(word_count[1])
	else:
		dict_list3[word_count[0]]=int(word_count[1])
	total_count_l3=total_count_l3+int(word_count[1])

dict_prob_list3={}

'Printing the word and word count in class 3 '
 
for key,val in dict_list3.items():
	unique=float(len(set(word3)))  # This takes the count of unique words in class 1
	prob_value=float(float(val+1)/(total_count_l3+unique)) 
	dict_prob_list3[key]=prob_value
	print "{} = {}".format(key, val)

print ' '


# List 4
word4=[]
for item in list4:
	word_count=item.split(':')
	word4.append(word_count[0])
	if(word_count[0] in dict_list4):
		dict_list4[word_count[0]]+=int(word_count[1])
	else:
		dict_list4[word_count[0]]=int(word_count[1])
	total_count_l4=total_count_l4+int(word_count[1])

dict_prob_list4={}

'Printing the word and word count in class 4 '
 
for key,val in dict_list4.items():
	unique=float(len(set(word4)))  # This takes the count of unique words in class 1
	prob_value=float(float(val+1)/(total_count_l4+unique)) 
	dict_prob_list4[key]=prob_value
	print "{} = {}".format(key, val)

print ' '



# List 5
word5=[]
for item in list5:
	word_count=item.split(':')
	word5.append(word_count[0])
	if(word_count[0] in dict_list5):
		dict_list5[word_count[0]]+=int(word_count[1])
	else:
		dict_list5[word_count[0]]=int(word_count[1])
	total_count_l5=total_count_l5+int(word_count[1])


dict_prob_list5={}

'Printing the word and word count in class 5 '
 
for key,val in dict_list5.items():
	unique=float(len(set(word5)))  # This takes the count of unique words in class 1
	prob_value=float(float(val+1)/(total_count_l5+unique)) 
	dict_prob_list5[key]=prob_value
	print "{} = {}".format(key, val)

print ' '


# List 6
word6=[]
for item in list6:
	word_count=item.split(':')
	word6.append(word_count[0])
	if(word_count[0] in dict_list6):
		dict_list6[word_count[0]]+=int(word_count[1])
	else:
		dict_list6[word_count[0]]=int(word_count[1])
	total_count_l6=total_count_l6+int(word_count[1])

dict_prob_list6={}

'Printing the word and word count in class 6 '
 
for key,val in dict_list6.items():
	unique=float(len(set(word6)))  # This takes the count of unique words in class 1
	prob_value=float(float(val+1)/(total_count_l6+unique)) 
	dict_prob_list6[key]=prob_value
	print "{} = {}".format(key, val)



# List 7
word7=[]
for item in list7:
	word_count=item.split(':')
	word7.append(word_count[0])
	if(word_count[0] in dict_list7):
		dict_list7[word_count[0]]+=int(word_count[1])
	else:
		dict_list7[word_count[0]]=int(word_count[1])
	total_count_l7=total_count_l7+int(word_count[1])


dict_prob_list7={}

'Printing the word and word count in class 7 '
 
for key,val in dict_list7.items():
	unique=float(len(set(word7)))  # This takes the count of unique words in class 1
	prob_value=float(float(val+1)/(total_count_l7+unique)) 
	dict_prob_list7[key]=prob_value
	print "{} = {}".format(key, val)


print' '
print '********************************************************************************************************************'
print ' '
print 'Printing the total count of words in different classes '
print ' '
print 'Total number of words in class 1 : ', total_count_l1 , '  unique words : ',len(set(word1))
print 'Total number of words in class 2 : ', total_count_l2 , '  unique words : ',len(set(word2))
print 'Total number of words in class 3 : ', total_count_l3 , '  unique words : ',len(set(word3))
print 'Total number of words in class 4 : ', total_count_l4 , '  unique words : ',len(set(word4))
print 'Total number of words in class 5 : ', total_count_l5 , '  unique words : ',len(set(word5))
print 'Total number of words in class 6 : ', total_count_l6 , '  unique words : ',len(set(word6))
print 'Total number of words in class 7 : ', total_count_l7 , '  unique words : ',len(set(word7))

# print the probabitiy values of different items in each list

# Class 1

print 'Printing the probability values in class 1'
for key,val in dict_prob_list1.items():
	print "{} = {}".format(key, val)
print ' '

# Class 2

print 'Printing the probability values in class 2'
for key,val in dict_prob_list2.items():
	print "{} = {}".format(key, val)

print ' '

# Class 3

print 'Printing the probability values in class 3'
for key,val in dict_prob_list3.items():
	print "{} = {}".format(key, val)

print ' '


# Class 4

print 'Printing the probability values in class 4'
for key,val in dict_prob_list4.items():
	print "{} = {}".format(key, val)

print ' '

# Class 5

print 'Printing the probability values in class 5'
for key,val in dict_prob_list5.items():
	print "{} = {}".format(key, val)

print ' '

# Class 6

print 'Printing the probability values in class 6'
for key,val in dict_prob_list6.items():
	print "{} = {}".format(key, val)

print ' '

# Class 7

print 'Printing the probability values in class 7'
for key,val in dict_prob_list7.items():
	print "{} = {}".format(key, val)

print ' '


# Now we have all the probability values and all we have to do is that we need to test how well our program works so let us take the test data now

# Read the testing data now
f=open("testingdata.txt","r+")

# We will follow the same pattern as we did for training. Put this elements into a list
# The objective is to find P(Class/Dataset)

# We will follow Bayes's rule and we will compare with all the probabilities to find the best one

print ' '
print ' '
print '*************************************************'
print ' Testing Begins Here  '
print '*************************************************'
print ' '
test_list=[]   #Initializing an empty list to take values from the training set.


for row in f.readlines():
	data=row.split()
	flag=0
	try:
		if(data[0].isdigit()):
			flag=1
		if(data[0]=='1'):
				val=1
		elif(data[0]=='2'):
			val=2
		elif(data[0]=='3'):
			val=3
		elif(data[0]=='4'):
			val=4
		elif(data[0]=='5'):
				val=5
		elif(data[0]=='6'):
			val=6
		elif(data[0]=='7'):
			val=7
	except IndexError :
		print 'Empty row'
	if(val==2):
		test_list.append(data[1])

print 'Now the Testing data is :'
print ' '
print test_list

print ' '
total_count_test=0 # To keep a count of the number of total words in the test list

dict_test={}
# Now put all the words in the given list to dictionary and we to get the count of each word and multiply that many times
for item in test_list:
	word_count=item.split(':')
	if(word_count[0] in dict_test):
		dict_test[word_count[0]]+=int(word_count[1])
	else:
		dict_test[word_count[0]]=int(word_count[1])
	total_count_test=total_count_test+int(word_count[1])

# Just to check whether we recieved all the values or not

print ' '
print 'Printing the words and their count from the given dataset '
print ' '
for key,val in dict_test.items():
	print "{} = {}".format(key, val)

# We need to take each word and find the probability. We should first begin from class 1
list_ygivenx = []    # to store the p(X/Y) values for each word so that at the end it can be multiplied
prob1=prob2=prob3=prob4=prob5=prob6=prob7=1
for key,val in dict_test.items():

	# P(X/1)

	if(key in dict_prob_list1):
		prob1=prob1*math.pow(float(dict_prob_list1[key]),int(val))
	else:
		unique=len(set(word1))
		prob1=prob1*math.pow(float(1.0/(total_count_l1+unique)),int(val))
	
	# P(X/2)

	if(key in dict_prob_list2):
		prob2=prob2*math.pow(float(dict_prob_list2[key]),int(val))
	else:
		unique=len(set(word2))
		prob2=prob2*math.pow(float(1.0/(total_count_l2+unique)),int(val))

	# P(X/3)

	if(key in dict_prob_list3):
		prob3=prob3*math.pow(float(dict_prob_list3[key]),int(val))
	else:
		unique=len(set(word3))
		prob3=prob3*math.pow(float(1.0/(total_count_l3+unique)),int(val))

	# P(X/4)

	if(key in dict_prob_list4):
		#print 'Value is ', float(dict_prob_list1[key])
		prob4=prob4*math.pow(float(dict_prob_list4[key]),int(val))
		#print 'prob 1 ', prob1
	else:
		unique=len(set(word4))
		prob4=prob4*math.pow(float(1.0/(total_count_l4+unique)),int(val))

	# P(X/5)

	if(key in dict_prob_list5):
		#print 'Value is ', float(dict_prob_list1[key])
		prob5=prob5*math.pow(float(dict_prob_list5[key]),int(val))
		#print 'prob 1 ', prob1
	else:
		unique=len(set(word5))
		prob5=prob5*math.pow(float(1.0/(total_count_l5+unique)),int(val))

	# P(X/6)

	if(key in dict_prob_list6):
		#print 'Value is ', float(dict_prob_list1[key])
		prob6=prob6*math.pow(float(dict_prob_list6[key]),int(val))
		#print 'prob 1 ', prob1
	else:
		unique=len(set(word6))
		prob6=prob6*math.pow(float(1.0/(total_count_l6+unique)),int(val))		

	# P(X/7)

	if(key in dict_prob_list7):
		#print 'Value is ', float(dict_prob_list1[key])
		prob7=prob7*math.pow(float(dict_prob_list7[key]),int(val))
		#print 'prob 1 ', prob1
	else:
		unique=len(set(word7))
		prob7=prob7*math.pow(float(1.0/(total_count_l7+unique)),int(val))	

# Having got all the P(X/Y) values multiply it with corresponding P(Y) values to get the result

list_ygivenx.append(prob1*prob_1)
list_ygivenx.append(prob2*prob_2)
list_ygivenx.append(prob3*prob_3)
list_ygivenx.append(prob4*prob_4)
list_ygivenx.append(prob5*prob_5)
list_ygivenx.append(prob6*prob_6)
list_ygivenx.append(prob7*prob_7)

# Printing the list with the probability values

print '****************************************************************'
print 'Printing the final probability matrix '

print list_ygivenx

print ' '

# Now we just need to find the class with maximum probability

max=0.0
j=1
final=0
for i in list_ygivenx:
	if(float(i)>max):
		max=i
		final=j
	j=j+1

print 'Now it is time for prediction '
print ' '
print '***************************************************************'
print ' '
print 'The class is : ',final
print ' '
print '***************************************************************'
print ' '