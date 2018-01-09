indieVar = input("Input the independent variables separated by a space: ")
indieVar = indieVar.split(" ")
channels = int(input("How many channels will be run through a given mold: "))

params = [0 for z in range(0,len(indieVar))]

for x in range(0,len(indieVar)):
	print("How many different", indieVar[x], "'s would you like to test?")
	params[x] = int(input(""))
	#This could be done easier with a dict

samples = 1

for x in params:
	samples *= x

if samples > 100:
	print("You have more than 100 samples, decrease one of the parameters and try again.")
else:
	print("There will be", samples, "samples needed and", int(samples/channels), "silicone molds needed")