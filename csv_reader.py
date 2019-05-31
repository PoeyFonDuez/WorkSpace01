#incase of using python 3 if 2 just pip install pandas
#1.sudo aptitude install python3-pip
#2.pip3 install pandas 
#pandas lib : For CSV file reading
import pandas, os
from pandas import DataFrame 

sth = pandas.read_csv("test info.csv", dtype = str) # read file as string type
#sth = pandas.read_csv("test info.csv", index_col ="Name")

print(sth) #print table
print(sth["Tel"][1]) #print column : sth[column name][index]
print(sth["Name"][1]) 

#write csv file use dictionary : list
Cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],
        "Dealer" : ["dealer1","dealer2","dealer3","dealer4"]
        }
df = DataFrame(Cars, columns = ["Brand","Price","Dealer"])# create table info DataFrame(dict)

filepath = os.getcwd()+"/test_write_file.csv" #os.getcwd() = get current filepath
export_csv = df.to_csv(r'filepath', index = None, header = True)
 # File writing - df.to_csv(r"filepath/filename.csv", index = None, header = True)


