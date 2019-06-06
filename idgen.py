import random,pandas,os
from pandas import DataFrame 

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
def savefile(id_list):
###input with list save id to CSV_file
	iddict = {"id":id_list}	
	df = DataFrame(iddict, columns = ["id"])
	filepath = os.getcwd()+"/id_gen.csv" 
	export_csv = df.to_csv(filepath, index = None, header = True)
	print(filepath)
	print(iddict)			

def mass_idgen(amount):
###amount selector which call citizen generator
	idlist = []
	num = 1
	for i in range(int(amount)):
		temp_id = id_generator()
		print(num," : ", temp_id)	
		num = num+1
		idlist.append(temp_id)
	print(idlist)	
	savefile(idlist)	
	mass_idgen(input("Gen More ID enter number / Exit Press CTRL + C: "))	
	return idlist


print("-------- This is citizen ID generator --------")
mass_idgen(input("Enter amout of ID you want: "))
