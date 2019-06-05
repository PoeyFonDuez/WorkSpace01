#text editor
#r = read,w = write,a = append if file not exist will create new one,+ = r/w for update
test_text = open("text_editor.txt","a+r") #open/create file in append+read mode
test_text.write("This is test text"+'\n')

#test_text = open("text_editor.txt","r")
#content = test_text.read() #file reading
content = test_text.readlines() #file reading line by line
print(content,type(content))

test_text.close()