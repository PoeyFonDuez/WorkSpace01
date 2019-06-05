#text editor
#r = read,w = write,a = append if file not exist will create new one,+ = r/w for update
#w : will overwrite old one , a : will update the file

test_text = open("text_editor.txt","w+") #open/create file in write+read mode
test_text.write("This is test text"+'\n') #str/list is available to write to file

test_text = open("text_editor.txt","r")
#content = test_text.read() #file reading
content = test_text.readlines() #file reading line by line
print(content,type(content))

test_text.close()

# #to change someline of file
# test_text = open("text_editor.txt","r")
# content = test_text.readlines()
# content[2] = "new text to change" #change data in line 2
# test_text = open("text_editor.txt","w")
# text_text.write(content) # write whole new file

