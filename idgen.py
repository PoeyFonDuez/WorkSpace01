import random

def id_generator():
###single citizen id generator
	counter = 13
	tempstr = ""
	tempsum = 0
	
	for i in range(12):
		if i == 0:
			tempint = random.randint(1,8)
			tempstr = tempstr + str(tempint)
			tempsum = tempsum + (tempint*counter)
			#print(tempstr, tempsum)
		else:
			tempint = random.randint(1,8)
			tempstr = tempstr + str(tempint)
			tempsum = tempsum + (tempint*counter)	
			#print(tempstr, tempsum)

		counter = counter-1
	#print(tempsum)	
	tempstr = tempstr + str(11 - (tempsum % 11))		
	#print(len(tempstr))
	if len(tempstr) == 13:		
		return(tempstr)
	else:
		return("-----Random Fail-----")
		
	#print(tempsum)
	#return tempstr
			

def mass_idgen(amount):
###amount selector which call citizen generator
	num = 1
	for i in range(int(amount)):
		print(num," : ", id_generator())	
		num = num+1
	
	mass_idgen(input("Gen More ID enter number / Exit Press CTRL + C: "))	

print("-------- This is citizen ID generator --------")
mass_idgen(input("Enter amout of ID you want: "))
