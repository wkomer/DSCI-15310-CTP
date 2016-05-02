#William Komer
#2-24-15
#Computation Thinking And Programming

#--ALGORITHIM 2--

list = [3,17,4,19,8,2];

i=0
x=0
g=3

while ( i < 6):
	#If I number = Number of box in list, Number in list > than G
	if( list[i] > g):
		g = list[i]
		x = i
	i=i+1
print g,",",x
