num=int(input("Enter a number to check collatz problem:"))

##defining a empty list to store all steps
tPoints=[]

##initializing while loop with a condition that exits when a final num value is equals to 1  because in collataz problem every number finally stucks in 4-2-1 loop
while num!=1:

	## here we're appending each num value to pre-defined tPoints list
	tPoints.append(int(num))

	##HERE WE CHECK NUM IS ODD OR EVEN
	if num%2==0: ##if it is even we divide it with 2
		num=num/2
	elif num%2==1:##if it is odd we substitute num in 3x+1(i.e, x=num)
		num=(3*num)+1

##Here we print no.of steps it took to complete collatz problem
print(f"It took {len(tPoints)} steps to complete")

##Here we print all the steps in its way to 1
print(f"Final list of points are {tPoints}")

##Here we asking to plot those steps in graphical view 
wPlot=input("Do you wish to plot these points and Visualize ??(type yes or no)")

if wPlot == "yes" or wPlot == "Yes" or wPlot=="YES":

	##importing pyplot package from matplotlib library
	from matplotlib import pyplot as plt

	##plot() function is from matplotlib package
	plt.plot(tPoints,"o-.")
	plt.show()
else:
	print("Thanks for not bothering ME 😅!!!")

