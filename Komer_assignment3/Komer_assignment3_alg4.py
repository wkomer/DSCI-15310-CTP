# William Komer
# February 25 2016
# Computational Thinking and Programming

#-- ALGORITHIM 4--

list = [6,8,4,5,2]

i = 0
j = 999

while ( i < 5 ):
	j = 0
	while( j < 4 ):
		k = j + 1
		if( list[j] > list[k] ):
			temp = list[j]
			list[j] = list[k]
			list[k] = temp
		j = j + 1
	print "List: ", list [i]
	i = i + 1
#used to checkthe output of the code.
#print list[0]
#print list[1]
#print list[2]
#print list[3]
#print list[4]
